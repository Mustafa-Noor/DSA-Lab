class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionParser:
    def __init__(self):
        self.operators = set(['+', '-', '*', '/', '^'])
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}  # Left/Right associativity

    def is_operator(self, c):
        return c in self.operators

    def infix_to_postfix(self, expression):
        stack = []
        output = []
        for char in expression.split():
            if char.isalnum():  # Operand (variable, number)
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Pop '('
            else:
                while (stack and stack[-1] != '(' and
                       (self.precedence[char] < self.precedence[stack[-1]] or
                        (self.precedence[char] == self.precedence[stack[-1]] and self.associativity[char] == 'L'))):
                    output.append(stack.pop())
                stack.append(char)

        while stack:
            output.append(stack.pop())
        return ' '.join(output)

    def construct_tree(self, expression):
        stack = []
        for token in expression.split():
            if not self.is_operator(token):
                node = Node(token)
                stack.append(node)
            else:
                node = Node(token)
                node.right = stack.pop()  # Right child first for binary operators
                node.left = stack.pop()  # Left child
                stack.append(node)
        return stack[-1]

    def print_prefix(self, node):
        if node:
            print(node.value, end=' ')
            self.print_prefix(node.left)
            self.print_prefix(node.right)

    def convert_to_prefix(self, expression):
        postfix_expression = self.infix_to_postfix(expression)
        root = self.construct_tree(postfix_expression)
        self.print_prefix(root)
        print()

# driver code

if __name__ == "__main__":
    parser = ExpressionParser()
    expression = "a + b * ( c - d )"
    print("Prefix notation:")
    parser.convert_to_prefix(expression)

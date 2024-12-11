class FinancialCalculator:
    def __init__(self):
        self.operators = set(['+', '-', '*', '/', '(', ')'])
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def preprocess_expression(self, expression):
        result = ""
        for i, ch in enumerate(expression):
            result += ch
            # Handle implicit multiplication
            if ch.isdigit() or ch == ')':
                if i + 1 < len(expression) and expression[i + 1] == '(':
                    result += '*'
        return result

    def tokenize(self, expression):
        tokens = []
        num = ""
        for ch in expression:
            if ch.isdigit():  
                num += ch
            else:
                if num:
                    tokens.append(num)  
                    num = ""
                if ch in self.operators or ch in "()":
                    tokens.append(ch)
        if num:
            tokens.append(num)
        return tokens

    def infix_to_postfix(self, expression):
        expression = self.preprocess_expression(expression)
        tokens = self.tokenize(expression)
        stack = []
        output = []
        for token in tokens:
            if token not in self.operators:
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and self.priority[token] <= self.priority.get(stack[-1], 0):
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return output

    def evaluate_postfix(self, expression):
        stack = []
        for token in expression:
            if token not in self.operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
        return stack[0]

    def calculate(self, expression):
        postfix = self.infix_to_postfix(expression)
        return self.evaluate_postfix(postfix)


if __name__ == "__main__":
    calc = FinancialCalculator()
    expression = input("Enter an arithmetic expression: ")
    try:
        result = calc.calculate(expression)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"Error: {e}")

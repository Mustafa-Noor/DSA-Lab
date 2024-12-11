class ExpressionConverter:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def __init__(self, expr):
        self.expr = expr

    def is_operator(self, ch):
        return ch in ['+', '-', '*', '/', '^']

    def is_operand(self, ch):
        return ch.isalnum()

    def infix_to_postfix(self):
        stack, postfix = [], []
        for ch in self.expr:
            if self.is_operand(ch):
                postfix.append(ch)
            elif ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                while stack and stack[-1] not in '([{':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] not in '([{' and self.precedence[ch] <= self.precedence.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(ch)
        while stack:
            postfix.append(stack.pop())
        return ''.join(postfix)

    def infix_to_prefix(self):
        rev_expr = self.expr[::-1]
        adj_expr = (rev_expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
                           .replace('[', 'temp').replace(']', '[').replace('temp', ']')
                           .replace('{', 'temp').replace('}', '{').replace('temp', '}'))
        postfix = ExpressionConverter(adj_expr).infix_to_postfix()
        return postfix[::-1]

    def postfix_to_infix(self, postfix):
        stack = []
        for ch in postfix:
            if self.is_operand(ch):
                stack.append(ch)
            else:
                op1, op2 = stack.pop(), stack.pop()
                stack.append(f'({op2}{ch}{op1})')
        return stack[-1]

    def prefix_to_infix(self, prefix):
        stack = []
        for ch in reversed(prefix):
            if self.is_operand(ch):
                stack.append(ch)
            else:
                op1, op2 = stack.pop(), stack.pop()
                stack.append(f'({op1}{ch}{op2})')
        return stack[-1]


# Example Usage
expr = "a+[(b*{c+[d-e]})/f]*g"
conv = ExpressionConverter(expr)

print("Infix Expression:", expr)
postfix = conv.infix_to_postfix()
print("Postfix Expression:", postfix)
prefix = conv.infix_to_prefix()
print("Prefix Expression:", prefix)
print("Converted to Infix from Postfix:", conv.postfix_to_infix(postfix))
print("Converted to Infix from Prefix:", conv.prefix_to_infix(prefix))

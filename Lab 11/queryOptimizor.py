
class QueryOptimizer:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}

    def infix_to_postfix(self, query):
        output = []
        stack = []
        tokens = query.split()

        for token in tokens:
            if token.isalnum():  # If the token is an operand, add it to the output
                output.append(token)
            elif token == '(':  # If the token is '(', push it to the stack
                stack.append(token)
            elif token == ')':  # If the token is ')', pop and output from the stack until '(' is found
                top_token = stack.pop()
                while top_token != '(':
                    output.append(top_token)
                    top_token = stack.pop()
            else:  # An operator is encountered
                while (stack) and (self.precedence[stack[-1]] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())
        
        return ' '.join(output)

if __name__ == "__main__":
    optimizer = QueryOptimizer()
    query = "SELECT * FROM table WHERE a + b * c"
    print("Infix Query: ", query)
    postfix_query = optimizer.infix_to_postfix(query)
    print("Postfix Query: ", postfix_query)
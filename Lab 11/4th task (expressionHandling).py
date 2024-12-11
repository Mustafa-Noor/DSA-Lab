import re

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    for token in expression:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isnumeric():
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
            elif token == '^':
                stack.append(a ** b)
    return stack[0]

def chatbot_response(query):
    # Extract the mathematical expression from the query
    expression = re.findall(r'\d+|\+|\-|\*|\/|\^|\(|\)', query)
    
    # Convert infix to postfix
    postfix_expression = infix_to_postfix(expression)
    
    # Evaluate the postfix expression
    result = evaluate_postfix(postfix_expression)
    
    return result

# Example usage
query = "What is (1+0)*5^2?"
result = chatbot_response(query)
print(f"Result for '{query}': {result}")

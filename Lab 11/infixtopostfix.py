def inToPost(expression):
    postfix = ""
    operatorStack = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            postfix += expression[i]
            i+=1
            continue

        token = expression[i]
        if token in operatorPrecedence:
            if token == ')':
                while operatorStack and operatorStack[-1]!='(':
                    operator = operatorStack.pop()
                    postfix+=operator
                operatorStack.pop()

            elif token == '(':
                operatorStack.append(token)
            else:
                while operatorStack and operatorStack[-1]!='(' and operatorPrecedence[token] <= operatorPrecedence[operatorStack[-1]]:
                    postfix += operatorStack.pop()
                operatorStack.append(token)

        i+=1
    
    while operatorStack:
        postfix += operatorStack.pop()

    return postfix

operatorPrecedence = {
        '(' : 1,
        ')' : 1,
        '^' : 4,
        '*' : 3,
        '/' : 3,
        '%' : 3,
        '+' : 2,
        '-' : 2
    }


if __name__ == "__main__":
    expression = input("Enter the infix expression: ")
    try:
        result = inToPost(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")


    expression = expression[::-1]  # Reverse the string
    expression = expression.replace(')', 'temp')  # Temporarily replace ')' to avoid conflict
    expression = expression.replace('(', ')')  # Replace '(' with ')'
    expression = expression.replace('temp', '(')  # Replace 'temp' with '('

    res = inToPost(expression)
    res = res[::-1]
    print(res)

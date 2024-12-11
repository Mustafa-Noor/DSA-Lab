def prefix(expression):
    operandStack = []
    operatorStack = []

    i = len(expression)-1

    while i>-1:
        if expression[i].isdigit():
            operandStack.append(int(expression[i]))
            i -=1
            continue
        if expression[i] == ' ':
            i -= 1
            continue
        
        token = expression[i]

        if token in operatorPrecedence:

            left = operandStack.pop()
            right = operandStack.pop()
            operator = token

            result = applyOperation(operator, left, right)
            operandStack.append(result)

        i -= 1

    

    return operandStack.pop()


def applyOperation(operator, left, right):
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        if right == 0:
            print("cant divide by zero")
            return None
        return left / right
    elif operator == '%':
        return left %  right
    elif operator == '^':
        return left**right
    else:
        print("Invalid operator!")
        return None


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
    expression = input("Enter the prefix expression: ")
    try:
        result = prefix(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
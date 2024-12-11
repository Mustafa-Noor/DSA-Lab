# can this be equal to the opposite of the front 

def postfix(expression):
    stack = []

    i= 0
    while i < len(expression):
        if expression[i] == ' ':
            i+=1
            continue
        if expression[i].isdigit():
            num = ''
            while i< len(expression) and expression[i].isdigit():
                num += expression[i] 
                i+=1
            stack.append(int(num))
            continue

        token = expression[i]
        if token in operatorPrecedence:
            right = stack.pop()
            left = stack.pop()
            result = applyOperation(token, left, right)
            stack.append(result)
        i+= 1

    return stack.pop()


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
    expression = input("Enter the postfix expression: ")
    try:
        result = postfix(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
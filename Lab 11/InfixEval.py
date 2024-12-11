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


def solveInfix(expression):

    operandStack = []
    operatorStack = []

    i = 0
    while i < len(expression):
        if expression[i] == " ":
            i+=1
            continue

        if expression[i].isdigit():
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i+=1

            operandStack.append(int(num))
            continue

        token = expression[i]

        if token in operatorPrecedence:
            if token == ')':
                while operatorStack and operatorStack[-1] != '(':
                    if len(operandStack) < 2:
                        print("Invalid expression because the length of the rem operands")
                        return
                    operator = operatorStack.pop()
                    right = operandStack.pop()
                    left = operandStack.pop()
                    result = applyOperator(operator, left, right)
                    operandStack.append(result)
                operatorStack.pop()
            elif token == '(':
                operatorStack.append(token)
            else:
                while operatorStack and operatorStack[-1]!='(' and operatorPrecedence[token] <= operatorPrecedence[operatorStack[-1]]:
                    if len(operandStack) < 2:
                        print("Invalid expression because the length of the rem operands")
                        return
                    operator = operatorStack.pop()
                    right = operandStack.pop()
                    left = operandStack.pop()
                    result = applyOperator(operator, left, right)
                    operandStack.append(result)
                operatorStack.append(token)
        i+=1

        while operatorStack:
            if len(operandStack) < 2:
                    print("Invalid expression because the length of the rem operands")
                    return
            operator = operatorStack.pop()
            right = operandStack.pop()
            left = operandStack.pop()
            result = applyOperator(operator, left, right)
            operandStack.append(result)


        return operandStack.pop()

                
        
    

def applyOperator(operator, left, right):
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
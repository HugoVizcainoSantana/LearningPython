from Week3_Class1 import *


def operand_stack_priority(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    if op == "^":
        return 3
    if op == "(":
        return 0


def operand_priority(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    if op == "^":
        return 4
    if op == "(":
        return 5


def insert_operand(postfix, operands, op):
    if len(operands) == 0:
        pushToStack(operands, op)
    else:
        if op == ")":
            while topFromStack(operands) != "(":
                postfix.append(popFromStack(operands))
            popFromStack(operands)
        elif len(operands) != 0 and (operand_stack_priority(topFromStack(operands)) < operand_priority(op)):
            pushToStack(operands, op)
        else:
            while len(operands) != 0 and operand_stack_priority(topFromStack(operands)) >= operand_stack_priority(op):
                postfix.append(popFromStack(operands))
            pushToStack(operands, op)


def operate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 // num2
    elif op == "^":
        return num1 ** num2
    else:
        return ArithmeticError


def solve_expression(string):
    expr = string.split()
    print("Expr:" + str(expr))
    postfix = []
    operands = []
    for e in expr:
        # print("Evaluating: " + e)
        if e.isdigit():
            postfix.append(int(e))
        else:
            insert_operand(postfix, operands, e)

    for e in operands:
        postfix.append(e)

    print("Postfix Notation:")
    print(postfix)
    result = []
    for e in postfix:
        print("Step: " + str(e))
        print(result)
        print(postfix)
        if isinstance(e, int):
            pushToStack(result, e)
        else:
            num2 = popFromStack(result)
            num1 = popFromStack(result)
            pushToStack(result, operate(num1, e, num2))

    return topFromStack(result)


# Example
print("""
##############################
# Evaluate Maths Expressions #
##############################
""")
expr1 = "5 + 8 * 9 - 3 * ( 6 - 4 )"
print("Solve " + expr1)
print(solve_expression(expr1))

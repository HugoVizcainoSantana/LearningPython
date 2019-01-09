def pushToStack(stack, element):
    """"
    Inserts Element at top of passed List, simulating a Stack
    Args:
        stack: List[T]
        element: T
    Return:
          List[T]: with element inserted
    """
    stack.append(element)
    return stack


def popFromStack(stack):
    """"
    Returns first element of the simulated Stack
    Args:
        stack: List[T]
    Return:
          List[T]: without first element
    """
    return stack.pop()


def topFromStack(stack):
    return stack[-1]


def enqueue(queue, element):
    queue.insert(0, element)
    return queue


def dequeue(queue):
    return queue.pop()


def topOfQueue(queue):
    return queue[-1]


def checkParenthesesParity(str):
    par_stack = []
    for e in str:
        if e == "(":
            pushToStack(par_stack, e)
        elif e == ")":
            try:
                popFromStack(par_stack)
            except IndexError:
                return "Not Balanced, Excess of \')\'"
    if len(par_stack) == 0:
        return "Balanced!"
    else:
        return "Not Balanced, Excess of \'(\'"


# Examples
string1 = "2+7*(3+1+5/(4-3))"  # Should return Balanced
string2 = "2+(7*(3+1+5/(4-3))"  # Should return Not balanced, Excess of (
string3 = "2+(7*(3+1+5/(4-3))))"  # Should return Not balanced, Excess of )
print(checkParenthesesParity(string1))
print(checkParenthesesParity(string2))
print(checkParenthesesParity(string3))

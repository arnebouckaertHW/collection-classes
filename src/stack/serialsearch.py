from stack.stack import *
from node.node import *

def serialsearch(a: stack, first: int, size: int, target):
    """Searches for a target value in 
    a stack of nodes starting at first.

    Args:
        a (stack): the stack to search
        first (int): the stack position at which the search will start
        size (int): the number of nodes to search
        target: the target value to search for

    Returns:
        int: if target appears in the stack, position of the node 
        that contains target; else -1
    """



    # set an int variable i to 0
    i = 1

    # set a boolean variable found to False
    found = False

    # while there are more elements to search
    # and the target has not been found
    # and i plus first does not exceed the length of the list
    while i <= size and not found and (i + first <= a.size() + 1):
        # if the current element is the target
        if node.listPosition(a.getHead(), i).getData() == target:
            # set found to True
            found = True
        # otherwise
        else:
            # increment i
            i += 1

    # check if the target was found
    if found:
        # return the index of the target
        return first + i - 1
    else:
        # return negative one
        return -1
from node.node import *
from stack.stack import *
from stack.serialsearch import *

class insertionsort():
    def insertionsort(data: stack, first: int):
        """Sorts a stack from smallest to largest bypassing
        th nodes to the left of first

        Args:
            data (stack): stack to be sorted
            first (int): the node position at 
            which the sort will begin
        """

        cursor = node.listPosition(data.getHead(), first)
        cursorposition = serialsearch(data, first, data.size(), cursor.getData()) + 1

        while cursorposition <= data.size():
            j = cursorposition

            while j > first and node.listPosition(data.getHead(), j - 1).getData() > node.listPosition(data.getHead(), j).getData():
                temp = node.listPosition(data.getHead(), j).getData()
                node.setDataAtPosition(data.getHead(), j, node.listPosition(data.getHead(), j - 1).getData())
                node.setDataAtPosition(data.getHead(), j - 1, temp)
                j -= 1

            cursorposition += 1
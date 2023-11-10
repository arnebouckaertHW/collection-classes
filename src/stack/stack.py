from node.node import *

class stack:
    """Stack class that uses a linked list of nodes as its underlying data structure.
    """

    def __init__(self):
        """Constructs an empty stack.

        :ivar __head: head of the stack
        :ivar __tail: tail of the stack
        :ivar __manyNodes: number of nodes in the stack
        """

        self.__head = None # reference to the top node in the stack
        self.__tail = self.__head # reference to the bottom node in the stack
        self.__manyNodes = 0 # keeps track of the number of nodes in the stack

    def size(self):
        """Returns the number of nodes in the stack.

        Returns:
            int: number of nodes in the stack
        """

        return self.__manyNodes

    def getHead(self):
        """Returns a reference to the head (top) of the calling stack.

        Returns: 
            node: reference to head (top) of the calling stack
        """

        return self.__head
    
    def getTail(self):
        """Returns a reference to the tail (bottom) of the calling stack.

        Returns:
            node: reference to tail (bottom) of the calling stack
        """

        return self.__tail
    
    def getData(self):
        """Returns the data values in the calling stack.

        Returns:
            str: data values in the calling stack
        """
        cursor = self.__head # used to step through the nodes in the calling stack
        data = "" # string representation of the data in the calling stack
        i = 1 # used to count the nodes in the calling stack

        # loop through the calling stack, one node at a time, getting
        # the data values and concatenating them to data
        while i <= self.size():
            data += str(cursor.getData()) + " "
            cursor = cursor.getLink()
            i += 1

        return data
    
    def __str__(self):
        """Returns a string representation of the calling stack.

        Returns:
            str: string representation of the calling stack
        """

        return f"[ {self.getData()}]"
    
    def push(self, element):
        """Pushes (adds) the specified element to the top of the calling stack.

        Args:
            element: specified element
        """

        # if the calling stack is empty
        if self.__head == None:
            # create a new node with the specified element
            self.__head = node(element, None)
            self.__tail = self.__head
        else:
            # create a new node with the specified element
            self.__head = node(element, self.__head)
    
        # get the number of nodes in the calling stack
        self.__manyNodes = node.listLength(self.__head)

    def isEmpty(self):
        """Determines whether the calling stack is empty.

        Returns:
            bool: True if the calling stack is empty, else False
        """

        return self.size() == 0
    
    def pop(self):
        """Removes and returns the element at the head (top) from the calling stack.

        Raises:
            ValueError: indicates calling stack is empty

        Returns:
            node: element at head (top) of the calling stack
        """

        
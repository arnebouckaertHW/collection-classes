from node.node import *

class queue:
    """queue class that uses a linked list of nodes as its underlying data structure.
    """

    def __init__(self):
        """Constructs an empty queue.

        :ivar __head: front of the queue
        :ivar __tail: rear of the queue
        :ivar __manyNodes: number of nodes in the queue
        """

        self.__head = None # reference to the front node in the queue
        self.__tail = self.__head # reference to the rear node in the queue
        self.__manyNodes = 0 # keeps track of the number of nodes in the queue

    def size(self):
        """Returns the number of nodes in the queue.

        Returns:
            int: number of nodes in the queue
        """

        return self.__manyNodes

    def getHead(self):
        """Returns a reference to the head (front) of the calling queue.

        Returns: 
            node: reference to head (front) of the calling queue
        """

        return self.__head
    
    def getTail(self):
        """Returns a reference to the tail (rear) of the calling queue.

        Returns:
            node: reference to tail (rear) of the calling queue
        """

        return self.__tail
    
    def getData(self):
        """Returns the data values in the calling queue.

        Returns:
            str: data values in the calling queue
        """
        cursor = self.__head # used to step through the nodes in the calling queue
        data = "" # string representation of the data in the calling queue
        i = 1 # used to count the nodes in the calling queue

        # loop through the calling queue, one node at a time, getting
        # the data values and concatenating them to data
        while i <= self.size():
            data += str(cursor.getData()) + " "
            cursor = cursor.getLink()
            i += 1

        return data
    
    def __str__(self):
        """Returns a string representation of the calling queue.

        Returns:
            str: string representation of the calling queue
        """

        return f"[ {self.getData()}]"
    
    def enqueue(self, element):
        """Inserts (adds) the specified element to the front of the calling queue.

        Args:
            element: specified element
        """

        # if the calling queue is empty
        if self.__head == None:
            # create a new node with the specified element
            self.__head = node(element, None)
            self.__tail = self.__head
        else:
            # add node to the front of the queue
            self.__tail.addNodeAfter(element)

            # advance the tail (rear) of the queue
            self.__tail = self.__tail.getLink()
    
        # get the number of nodes in the calling queue
        self.__manyNodes = node.listLength(self.__head)

    def isEmpty(self):
        """Determines whether the calling queue is empty.

        Returns:
            bool: True if the calling queue is empty, else False
        """

        return self.size() == 0
    
    def dequeue(self):
        """Removes and returns the element at the head (front) from the calling queue.

        Raises:
            ValueError: indicates calling queue is empty

        Returns:
            _type_: element at head (front) of the calling queue
        """

        try:
            # if the calling queue is empty, raise error
            if self.isEmpty():
                raise ValueError("queue is empty")
        except ValueError as error:
            exit(error)
        else:
            # get data in node at the head (front) of the calling queue
            front = self.__head.getData()

            # remove the node at the head (front) of the calling queue
            self.__head = self.__head.getLink()

            # recompute the number of nodes in the calling queue
            self.__manyNodes = node.listLength(self.__head)

            # return data in node at the head (front) of the calling queue
            return front
        
    def peek(self):
        """Returns the element at the head (front) of the calling queue.

        Raises:
            ValueError: indicates calling queue is empty

        Returns:
            _type_: element at head (front) of the calling queue
        """

        try:
            # if the calling queue is empty, raise error
            if self.isEmpty():
                raise ValueError("queue is empty")
        except ValueError as error:
            exit(error)
        else:
            # return data in node at the head (front) of the calling queue
            return self.__head.getData()
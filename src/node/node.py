class node:
    """The node class holds a collection of values using nodes. It includes
     methods that allow the nodes to be manipulated and modified.
    """

    def __init__(self, data, link):
        """Constructs a node using the specified data value and link.

        :ivar __data: specified data value
        :ivar __link: link portion of node

        Args:
            data: specified data value
            link: specified link
        """

        self.__data = data
        self.__link = link

    def getData(self):
        """Returns the data value of the calling node.

        Returns: 
            _type_: data value of the node
        """

        return self.__data

    def setData(self, data):
        """Sets the data value of the calling node 
        to the specified data value.

        Args:
            data (_type_): specified data value
        """

        self.__data = data

    def getLink(self):
        """Returns the link of the calling node.

        Returns:
            node: link of the node
        """

        return self.__link
    
    def setLink(self, link):
        """Sets the link of the calling node to the specified link.

        Args:
            link (node): specified link
        """

        self.__link = link

    def addNodeAfter(self, element):
        """Adds a new node after the calling node using the specified element.

        Args:
            element (_type_): specified element
        """

        self.__link = node(element, self.__link)

    def removeNodeAfter(self):
        """Removes the node after the calling node."""

        self.__link = self.__link.__link

    @staticmethod
    def listLength(head):
        """COmputes and returns the number of nodes in a specified node.

        Args:
            head (node): specified head

        Returns:
            int: number of nodes in the specified node
        """

        cursor = head # cursor used to step through the specified node
        length = 0 # used to count the number of nodes in the specified node

        while cursor != None:
            # increment length
            length += 1

            # move cursor to the next node
            cursor = cursor.getLink()

        return length
    
    @staticmethod
    def listSearch(head, target):
        """Searches for a specified target in a specified node.

        Args:
            head (node): specified head
            target: specified target

        Returns:
            node: reference to node that contains specified target value
            if specified target is found, else None 
        """

        cursor = head # cursor used to step through the specified node

        while cursor != None:
            if cursor.getData() == target:
                return cursor
            else:
                cursor = cursor.getLink()
        
        return None
    
    @staticmethod
    def listPosition(head, position: int):
        """Searches for a node in a specified node based on a specified position.

        Args:
            head (node): specified head
            position (int): specified position

        Raises:
            ValueError: if specified position is less than one

        Returns:
            node: reference to node at specified position if specified position is found,
            else None
        """

        cursor = head # cursor used to step through the specified node
        count = 1 # used to count the number of nodes in the specified node

        try:
            # if specified position is less than one, raise ValueError
            if position < 1:
                raise ValueError("Position must be >= 1")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:
            # move cursor the correct nuùber of nodes
            # as long as count is less than specified position and 
            # cursor is not None
            # if cursor is None, that means the specified position
            # is greater than the number of nodes in the specified node
            while cursor != None and count < position:
                # move the cursor to the next node
                cursor = cursor.getLink()

                # increment counter variable
                count += 1

            # return cursor
            return cursor
        
    @staticmethod
    def listCopy(source):
        """Copies a specified node.

        Args:
            source (node): specified head

        Returns:
            node: reference to the head node in the copy
        """

        # if specified source node is None, return None
        if source == None:
            return None
        
        # make copy head refer to a node that contains the same
        # data value as the source node
        copyHead = node(source.getData(), None)

        # make copy tail refer to the same node as copy head
        copyTail = copyHead

        # keep looping through the specified source node to be copied
        # until we reach the node that has a link of none
        while source.getLink() != None:
            # advance to the next node in tje specified source node to be copied
            source = source.getLink()

            # get the data value in the specified source node and add
            # it to the end of copy tail
            copyTail.addNodeAfter(source.getData())

            # advance the copy tail to the next node
            copyTail = copyTail.getLink()
        
        # return copy head
        return copyHead
    
    @staticmethod
    def listCopyWithTail(source):
        """Copies a specified node and returns the head and tail reference.

        Args:
            source (node): specified head

        Returns:
            list: list with reference to the head node in the copy 
            and reference to the tail node in the copy
        """

        # if specified source node is None, return None
        if source == None:
            return None, None
        
        # make copy head refer to a node that contains the same
        # data value as the source node
        copyHead = node(source.getData(), None)

        # make copy tail refer to the same node as copy head
        copyTail = copyHead

        # keep looping through the specified source node to be copied
        # until we reach the node that has a link of none
        while source.getLink() != None:
            # advance to the next node in tje specified source node to be copied
            source = source.getLink()

            # get the data value in the specified source node and add
            # it to the end of copy tail
            copyTail.addNodeAfter(source.getData())

            # advance the copy tail to the next node
            copyTail = copyTail.getLink()
        
        # return copy head and copy tail
        return [copyHead, copyTail]
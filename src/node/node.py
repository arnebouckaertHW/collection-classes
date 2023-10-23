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
            _type_: link of the node
        """

        return self.__link
    
    def setLink(self, link):
        """Sets the link of the calling node to the specified link.

        Args:
            link (_type_): specified link
        """

        self.__link = link

    
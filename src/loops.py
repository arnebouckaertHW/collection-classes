class loops:
    @staticmethod
    def evens (start: int, end: int):
        """Finds and displays the even numbers between a specified
        starting and ending value.
        
        Args:
            start (int): specified starting value
            end (int): specified ending value
        """

        i = start
        while (i <= end):
            if (i % 2 == 0):
                print(i, end=" ")
        
            i += 1
from queues.queue import *
from stack.stack import *

class queuePalindrome:
    @staticmethod
    def isPalindrome(expression: str):
        """Checks if the given expression reads the same forward and backward.

        Args:
            expression (str): specified expression

        Returns:
            Boolean: True if the specified expression is a palindrome, else False
        """

        q1 = queue() # queue to read the expression forward
        q2 = queue() # second queue to read the expression backward

        mismatches = 0 # used to keep track of the differences in the queues
        # convert expression to uppercase
        expression = expression.upper()

        # loop through the expression a character at a time
        for e in expression:
            # if the character is an alphabetic character, add it to the first queue
            if e.isalpha():
                q1.enqueue(e)

        # loop through the expression a character at a time in reverse
        for e in expression[::-1]:
            # if the character is an alphabetic character, add it to the second queue
            if e.isalpha():
                q2.enqueue(e)

        # while the queue is not empty
        while not q1.isEmpty():
            # if the queue and stack do not match, increment mismatches
            if q1.dequeue() != q2.dequeue():
                mismatches += 1

        # return True if there are no mismatches, else False
        return mismatches == 0
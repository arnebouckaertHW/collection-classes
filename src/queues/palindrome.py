from queues.queue import *
from stack.stack import *

class palindrome:
    @staticmethod
    def isPalindrome(expression: str):
        """Checks if the given expression reads the same forward and backward.

        Args:
            expression (str): specified expression

        Returns:
            Boolean: True if the specified expression is a palindrome, else False
        """

        q = queue() # queue to read the expression forward
        s = stack() # stack to read the expression backward

        mismatches = 0 # used to keep track of the differences in the queue and stack

        # convert expression to uppercase
        expression = expression.upper()

        # loop through the expression a character at a time
        for e in expression:
            # if the character is an alphabetic character, add it to the queue and stack
            if e.isalpha():
                q.enqueue(e)
                s.push(e)

        # while the queue is not empty
        while not q.isEmpty():
            # if the queue and stack do not match, increment mismatches
            if q.dequeue() != s.pop():
                mismatches += 1

        # return True if there are no mismatches, else False
        return mismatches == 0
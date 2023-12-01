from queues.queue import *
from stack.stack import *

class advancedpalindrome:
    @staticmethod
    def isPalindrome(expression: str):
        """Checks if the given expression reads the same forward and backward.

        Args:
            expression (str): specified expression

        Returns:
            Boolean: True if the specified expression is a palindrome, else False
            str: the expression up to the point where it is no longer a palindrome or the full expression if it is a palindrome
        """

        q = queue() # queue to read the expression forward
        s = stack() # stack to read the expression backward
        line = queue() # queue to store the expression up to the point where it is no longer a palindrome

        lineStr = "" # string to store the expression up to the point where it is no longer a palindrome

        isPalindrome = True # used to keep track of whether the expression is a palindrome or not

        # loop through the expression a character at a time
        for e in expression:
            # if the character is an alphabetic character, add it to the queue and stack
            if e.isalpha():
                # only add the upper case version of the character to the queue and stack to make the comparison case insensitive
                q.enqueue(e.upper())
                s.push(e.upper())
                line.enqueue(e)

        # while the queue is not empty
        while not q.isEmpty() and isPalindrome != False:
            # if the queue and stack do not match, increment mismatches
            if q.dequeue() != s.pop():
                isPalindrome = False
            lineStr += line.dequeue()

        return isPalindrome, lineStr
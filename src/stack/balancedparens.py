from stack.stack import *

class balancedparens:
    @staticmethod
    def isBalanced(expression: str):
        """Checks a specified mathematical expression to see if it has balanced parentheses.

        Args:
            expression (str): specified expression

        Returns:
            bool: True if the specified expression has balanced parentheses, 
            else False
        """

        # variables for parentheses
        LEFT_NORMAL = "("
        RIGHT_NORMAL = ")"
        LEFT_SQUARE = "["
        RIGHT_SQUARE = "]"
        LEFT_CURLY = "{"
        RIGHT_CURLY = "}"

        # stack used to store parentheses
        store = stack()

        # variable used to indicate imbalance
        imbalance = False

        # loop through the specified expression, one character at a time
        # as long as there isn't an imbalance
        for s in expression:
            if not imbalance:
                if s == LEFT_CURLY or s == LEFT_NORMAL or s == LEFT_SQUARE:
                    # if the current character is a {, (, or [, push it onto the stack
                    store.push(s)
                elif s == RIGHT_NORMAL:
                    # if the current character is a ), check if the stack is empty
                    # or if the top node doesn't contain a (
                    if store.isEmpty() or store.pop() != LEFT_NORMAL:
                        imbalance = True
                elif s == RIGHT_SQUARE:
                    # if the current character is a ], check if the stack is empty
                    # or if the top node doesn't contain a [
                    if store.isEmpty() or store.pop() != LEFT_SQUARE:
                        imbalance = True
                elif s == RIGHT_CURLY:
                    # if the current character is a }, check if the stack is empty
                    # or if the top node doesn't contain a {
                    if store.isEmpty() or store.pop() != LEFT_CURLY:
                        imbalance = True
        
        # return True if the stack is empty and there isn't an imbalance
        return store.isEmpty() and not imbalance

from stack.stack import *

class calculator:
    @staticmethod
    def evaluate(expression: str):
        """Evaluate a specific mathematical expression.

        Args:
            expression (str): specified mathematical expression

        Returns:
            float: result of the specified mathematical expression
        """

        # create stack to store numbers
        numbers = stack()

        # create stack to store operators
        operators = stack()

        # loop through the specified mathematical expression, one character at a time
        for s in expression:
            # if the current character is a number
            if s.isnumeric():
                # push the current character to numbers
                numbers.push(float(s))
            # if the current character is an operator
            elif s == "+" or s == "-" or s == "*" or s == "/":
                # push the current character to operators
                operators.push(s)
            # if the current character is a closing parenthesis
            elif s == ")":
                # evaluate stacks
                calculator.evaluateStackTops(numbers, operators)
            elif s != "(":
                # exit if the current character is invalid
                exit("Illegal input expression!")
        
        # exit if the numbers stack doesn't have exactly one number
        if numbers.size() != 1:
            exit("Illegal input expression!")

        # return the result of the specified mathematical expression
        return numbers.pop()

    @staticmethod
    def evaluateStackTops(numbers, operators):
        """Applies an operation taken from the specified operators stack 
        to the top two numbers from the specified numbers stack.

        Args:
            numbers (stack): specified numbers stack
            operators (stack): specified operators stack
        """

        # exit if the numbers stack doesn't have at least two numbers
        # or the operators stack doesn't have at least one operator
        if numbers.size() < 2 or operators.isEmpty():
            exit("Illegal input expression!")

        # assign the number at the top of the numbers stack to opperand2
        operand2 = numbers.pop()

        # assign the number at the top of the numbers stack to opperand1
        operand1 = numbers.pop()

        # assign the operator at the top of the operators stack to operator
        operator = operators.pop()

        if operator == "+":
            # push the sum of operand1 and operand2 to numbers
            numbers.push(operand1 + operand2)
        elif operator == "-":
            # push the difference of operand1 and operand2 to numbers
            numbers.push(operand1 - operand2)
        elif operator == "*":
            # push the product of operand1 and operand2 to numbers
            numbers.push(operand1 * operand2)
        elif operator == "/":
            # push the quotient of operand1 and operand2 to numbers
            numbers.push(operand1 / operand2)
        else:
            # exit if the operator is invalid
            exit("Illegal input expression!")
import numpy as np
from flask import jsonify


class BasicMath:
    """This class performs basic math operations (selected by user)  on operands given.
    For example,
    a = 5, b = 2
    operation = "addition"
    addition(a, b)
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def format_results(result):
        ans_dict = {"ans": result}
        return jsonify(ans_dict)

    def add(self, op1=None, op2=None):
        """
        Parameters
        ----------
        op1 : type= num,  first operand for addition operation
        op2 : type= num,  second operand for addition  operation

        Returns: jsonfied numerical sum of a and b. For example add(5, 2) returns 7.
        -------

        """
        if op1 is not None:
            self.a = op1
        if op2 is not None:
            self.b = op1

        result = self.a + self.b
        return BasicMath.format_results(result)

    def subtract(self, op1=None, op2=None):
        """
        Parameters
        ----------
        op1 : type= num,  first operand for subtraction operation
        op2 : type= num,  second operand for subtraction  operation

        Returns: numerical difference of a and b. For example subtract(5, 2) returns 3.
        -------
        """
        if op1 is not None:
            self.a = op1
        if op2 is not None:
            self.b = op1

        result = self.a - self.b
        return BasicMath.format_results(result)

    def multiply(self, op1=None, op2=None):
        """
        Parameters
        ----------
        op1 : type= num,  first operand for multiplication operation
        op2 : type= num,  second operand for multiplication  operation

        Returns: type= num, umerical product of a and b. For example, multiply(5, 2) return 10.
        -------
        """
        if op1 is not None:
            self.a = op1
        if op2 is not None:
            self.b = op1

        result = self.a * self.b
        return BasicMath.format_results(result)

    def divide(self, op1=None, op2=None):
        """

        Parameters
        ----------
        op1: type=num, first operand for division operation
        op2: type=num, second operand for division operation, must be greater than zero otherwise ZeroDivisionError exception is raised

        Returns: quotient of division of a by b
        -------

        """
        if op1 is not None:
            self.a = op1
        if op2 is not None:
            self.b = op1
        try:
            result = self.a / self.b
            return BasicMath.format_results(result)
        except ZeroDivisionError:
            print(f"You are trying to divide {self.a} by zero which is not allowed")

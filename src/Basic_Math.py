import numpy as np
from flask import jsonify


class BasicMath:
    """This class performs basic math operations (selected by user)  on operands given.
    For example,
    a = 5, b = 2
    operation = "addition"
    addition(a, b)
    """

    def __init__(self):
        print("")

    @classmethod
    def format_results(cls, result):
        ans_dict = {"ans": result}
        return jsonify(ans_dict)

    def add(self, a, b):
        """

        Parameters
        ----------
        a : type= num,  first operand for addition operation
        b : type= num,  second operand for addition  operation

        Returns: numerical sum of a and b. For example add(5, 2) returns 7.
        -------

        """
        result = a + b
        return jsonify(result)

    def subtract(self, a, b):
        """
        Parameters
        ----------
        a : type= num,  first operand for subtraction operation
        b : type= num,  second operand for subtraction  operation

        Returns: numerical difference of a and b. For example subtract(5, 2) returns 3.
        -------
        """
        result = a - b
        return jsonify(result)

    def multiply(self, a, b):
        """
        Parameters
        ----------
        a : type= num,  first operand for multiplication operation
        b : type= num,  second operand for multiplication  operation

        Returns: type= num, umerical product of a and b. For example, multiply(5, 2) return 10.
        -------
        """
        result = a * b
        return jsonify(result)

    def divide(self, a, b):
        """

        Parameters
        ----------
        a: type=num, first operand for division operation
        b: type=num, second operand for division operation, must be greater than zero otherwise ZeroDivisionError exception is raised

        Returns: quotient of division of a by b
        -------

        """
        try:
            result = a / b
            return jsonify(result)
        except ZeroDivisionError:
            print(f"You are trying to divide {a} by zero which is not allowed")




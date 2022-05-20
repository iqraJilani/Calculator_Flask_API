import numpy as np
from flask import jsonify


class Basic_Math:
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


class Np_Math(Basic_Math):
    """
    This class performs mathemtical operations on array and matrix data

    """

    def __init__(self, np_data):
        self.np_data = np_data

    def add(self, a, b):
        """

        Parameters
        ----------
        a: type = array or matrix , first operand for numpy addition operation.
        b: type = array or matrix, second operand for numpy addition operation.

        Returns: type = numpy array or matrix, addition result of arguments given
        -------

        """
        if not self.np_data:
            return super.add(a, b)
        else:
            try:
                a = np.array(a)
                b = np.array(b)
                result = (a + b).tolist()
                return jsonify(result)
            except ValueError as e:
                return jsonify(str(e))

    def subtract(self, a, b):
        """

        Parameters
        ----------
        a: type = array or matrix, first operand for numpy subtraction operation.
        b: type = array or matrix, second operand for numpy subtraction  operation.

        Returns: type = numpy array or matrix, subtraction result of arguments given
        -------

        """
        if not self.np_data:
            return super.subtract(a, b)
        else:
            try:
                a = np.array(a)
                b = np.array(b)
                result = (a - b).tolist()
                return jsonify(result)
            except ValueError as e:
                return jsonify(str(e))

    def multiply(self, a, b):
        """
        Parameters
        ----------
        a: type = array or matrix , first operand for numpy matrix or element wise multiplication operation.
        b: type = array or matrix, second operand for numpy matrix or element wise multiplication operation.

        Returns: type = numpy array or matrix, result of matrix or element wise multiplication of arguments given.
        -------
        """
        # try:
        #     a = np.array(a)
        #     b = np.array(b)
        #     if len(a.shape) and len(b.shape) == 1:
        #         result = (np.multiply(a, b)).tolist()
        #     else:
        #         result = (np.dot(a, b)).tolist()
        #     return result
        # except ValueError as e:
        #     return str(e)
        if not self.np_data:
            return super.multiply(a, b)
        else:
            try:
                a = np.array(a)
                b = np.array(b)
                result = (np.dot(a, b)).tolist()
                return jsonify(result)
            except ValueError as e:
                return jsonify(str(e))

    def divide(self, a, b):
        """
        Parameters
        ----------
        a: type = array or matrix , first operand for numpy division operation.
        b: type = array or matrix, second operand for numpy division operation.

        Returns: type = numpy array or matrix, division result of arguments given
        -------
        """
        if not self.np_data:
            return super.divide(a, b)
        else:
            try:
                a = np.array(a)
                b = np.array(b)
                result = (a / b).tolist()
                return jsonify(result)
            except ValueError as e:
                return jsonify(str(e))

from Basic_Math import BasicMath
import numpy as np
from flask import jsonify


class NpMath(BasicMath):
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

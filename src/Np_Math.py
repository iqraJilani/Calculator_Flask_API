from .Basic_Math import BasicMath
import numpy as np


class NpMath(BasicMath):
    """
    This class performs mathematical operations on array and matrix data

    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, np_data, op1=None, op2=None):
        """

        Parameters
        ----------
        op1: type = array or matrix , first operand for numpy addition operation.
        op2: type = array or matrix, second operand for numpy addition operation.
        np_data: type = boolean flag to check if arguments are numpy arrays or not

        Returns: type = numpy array or matrix, addition result of arguments given
        -------

        """
        if op1 is not None:
            self.a = op1
        if op2 is not None:
            self.b = op1

        if not np_data:
            result = super.add(self.a, self.b)
        else:
            try:
                self.a = np.array(self.a)
                self.b = np.array(self.b)
                result = (self.a + self.b).tolist()
                result = BasicMath.format_results(result)
            except ValueError as e:
                result = BasicMath.format_results(str(e))
        return result

    def subtract(self, np_data, op1=None, op2=None):
        """

        Parameters
        ----------
        op1: type = array or matrix, first operand for numpy subtraction operation.
        op2: type = array or matrix, second operand for numpy subtraction  operation.
        np_data: type = boolean flag to check if arguments are numpy arrays or not

        Returns: type = json data of numpy array or matrix, subtraction result of arguments given
        -------

        """
        if op1 is not None:
            self.a = op1
        if op2 is not None:
            self.b = op1

        if not np_data:
            result = super.subtract(self.a, self.b)
        else:
            try:
                self.a = np.array(self.a)
                self.b = np.array(self.b)
                result = (self.a - self.b).tolist()
                result = BasicMath.format_results(result)
            except ValueError as e:
                result = BasicMath.format_results(str(e))

        return result

    def multiply(self, np_data, op1=None, op2=None):
        """
        Parameters
        ----------
        op1: type = array or matrix , first operand for numpy matrix or element wise multiplication operation.
        op2: type = array or matrix, second operand for numpy matrix or element wise multiplication operation.
        np_data: type = boolean flag to check if arguments are numpy arrays or not

        Returns: type = json data of numpy array or matrix, result of matrix or element wise multiplication of
        arguments given. -------
        """
        if op1 is not None:
            self.a = op1
        if op2 is not None:
            self.b = op1

        if not np_data:
            result = super.multiply(self.a, self.b)
        else:
            try:
                self.a = np.array(self.a)
                self.b = np.array(self.b)
                result = (np.dot(self.a, self.b)).tolist()
                result = BasicMath.format_results(result)
            except ValueError as e:
                result = BasicMath.format_results(str(e))
        return result

    def divide(self, np_data, op1=None, op2=None):
        """
        Parameters
        ----------
        op1: type = array or matrix , first operand for numpy division operation.
        op2: type = array or matrix, second operand for numpy division operation.
        np_data: type = boolean flag to check if arguments are numpy arrays or not

        Returns: type = json data of numpy array or matrix, division result of arguments given
        -------
        """
        if op1 is not None:
            self.a = op1
        if op2 is not None:
            self.b = op1

        if not np_data:
            return super.divide(self.a, self.b)
        else:
            try:
                self.a = np.array(self.a)
                self.b = np.array(self.b)
                result = (self.a / self.b).tolist()
                result = BasicMath.format_results(result)
            except ValueError as e:
                result = BasicMath.format_results(str(e))
        return result

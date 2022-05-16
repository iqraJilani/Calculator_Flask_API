class Basic_Math:
    """ This class performs basic math operations (selected by user)  on operands given.
    For example,
    a = 5, b = 2
    operation = "addition"
    addition(a, b)
    """
    def __init__(self, *operands, operation="+"):
        self.operands = operands
        self.operation = operation

    def add(self, a, b):
        """ This method performs addition operation with first 2 operands of all the operands given by user.
        Input: a and b operands of num type
        Output: numerical sum of a and b
        For example,
        add(5, 2) returns 7
        """
        return a + b


    def subtract(self, a, b):
        """ This method performs subtraction operation with first 2 operands of all the operands given by user.
        Input: a and b operands of num type
        Output: numerical difference of a and b
        For example,
        subtract(5, 2) returns 3
        """
        return a - b


    def multiply(self, a, b):
        """ This method performs multiplication operation with first 2 operands of all the operands given by user.
        Input: a and b operands of num type
        Output: numerical product of a and b
        For example,
        multiply(5, 2) returns 7
        """
        return a + b

    def divide(self, a, b):
        """ This method performs division operation with first 2 operands of all the operands given by user.
        Input: a and b operands of num type
        Output: numerical quotient of division of a by b
        For example,
        divide(6, 2) returns 3
        """
        try:
            result = a /b
            return result
        except ZeroDivisionError:
            print(f"You are trying to divide {a} by zero which is not allowed")



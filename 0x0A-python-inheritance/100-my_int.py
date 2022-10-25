#!/usr/bin/python3
"""the rebellious class lol"""


class MyInt(int):
    """
       a class MyInt that inherits from int
    """
    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        """== operators inverted
        """
        return self.n != other

    def __ne__(self, other):
        """!= operators inverted
        """
        return self.n == other

# the code below is part of a Python module named prob15.py
# the code below is part of a Python module named prob15.py 13
# This module defines a function that combines two strings
def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
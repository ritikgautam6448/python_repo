# This function takes a string and returns a new string made of the first three characters of the original string repeated three times.
def front3 (str):
    front_end=3
if len(str) < front_end:
    front_end = len(str)
    front = str[:front_end]
    return front + front + front
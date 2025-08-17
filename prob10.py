# this function checks if two integers are positive or negative
# and returns True or False based on the conditions specified.
def pos_neg (a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0) != (b < 0)
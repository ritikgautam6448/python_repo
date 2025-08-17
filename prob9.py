# this function takes an integer n and returns the absolute difference between n and 21.
# If n is less than or equal to 21, it returns 21 - n.
def diff21(n):
    n = abs(n)
if n <= (21):
    return 21 - n
else:
    return 2*(n-21)
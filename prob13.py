#this function takes two strings and returns a new string
#that concatenates the two strings, omitting the first character of each.
def non_start(a, b):
   if len (a) < len(b):
       return a + b + a
   else:
       return b + a + b
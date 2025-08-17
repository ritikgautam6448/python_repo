# this function takes a string and returns a new string with the first and last characters swapped.
def front_back(str):
    if len(str)<=1:
      return str
mid=str [1:len (str)-1]
return str [str(str)-1]+mid +str[0]
# that spans across
def front_back(s):
    if len(s) <= 1:
        return s
    
    mid = s[1:len(s)-1]   # middle part (excluding first and last char)
    return s[-1] + mid + s[0]  # last + middle + first


print(front_back("code"))  # Expected: eodc
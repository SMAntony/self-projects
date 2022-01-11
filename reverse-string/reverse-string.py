_str = str(input("Enter the string to reverse: "))

# using slicing
print("Reverse String using slicing:",_str[::-1])

print("-"*60)

# naive approach
n = len(_str)
_str1 = ""
for i in range(n):
    _str1 = _str1 + _str[n-i-1]
    print("Iteration",i,_str1)
print("Reverse String, naive approach", _str1)
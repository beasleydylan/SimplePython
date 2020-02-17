import math
str1 = str(math.pi)
x = int(input('How many decimal places past pi? Max is 15: '))
if x > 15:
    x = 15
print(str1[0:x+2])
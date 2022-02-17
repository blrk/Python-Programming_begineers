"""
if statement 
"""
"""
if condition:
    statement(s)
"""
num = -1

if num > 0:
    print(num, " is a postive number")
print("This line always executed") # next statement 

"""
if else statement

if condition:
    body of if
else:
    body of else
"""
num = -1

if num >= 0:
    print(num, " is a postive or zero")
else:
    print(num, "is Negative")
print("This line always executed") # next statement  

"""
if .. elif else staement

if condition1:
    body of if
elif condtion 2:
    body of elif
else:
    body of else
"""

num = -1

if num > 0:
    print(num, " is a postive number")
elif num == 0:
    print("zero")
else:
    print(num, " is negative")
print("This line always executed") # next statement 

"""
nested if statement

if statement inside another if statment 
"""

num = int(input("enter a number:"))
if num >= 0: # outer if 
    if num == 0: # inner if 
        print("zero")
    else:
        print(num, "is a postive number")
else: 
    print(num, " negative")
print("This line always executed") # next statement 

"""
list
"""
l1 = [13, 4, 2, 56] # list 
print(type(l1))

for i in range(len(l1)):
    print(l1[i])
    
print("lenght of l1", len(l1))

l1.sort()
print(l1)


"""
pattern
"""
for i in range(1, 6): # 1 to 5
    for j in range(1, i+1): # 1 to 2
        print(i, end= " ")
    print("")

str1 = "etst"
str2 = sorted(str1)
str2
type(str2)





























    
        


















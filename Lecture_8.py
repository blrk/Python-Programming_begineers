# Lecture-8
"""
Strings
accessing Characters and Substrings in Strings

python string --> data structure
string --> sequence of characters or zero or more characters 
"""
str1 = "Welcome"
str2 = 'w'

print(type(str1))
print(type(str2))

# how to find the length of the string

print("length of str1:", len(str1))
print("length of str1:", len(str2))

print(len(""))
print(len(" "))

str3 = "Karunya University"

"""
K a r u n y a   U n i  v  e  r  s  i  t  y
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 --> index value 
"""
print(len(str3))

# the subscript operator

# <a string> [<an integer / integer expression>] --> index 
print(str3)

str3[0]

str3[4]

str3[1+5]

str3[len(str3)] # string index out of range 
# trying to access an index that does not exist

str3[len(str3) - 1]

str3[-1] # shorthand for the last character

str3[-2] # shorthand for next to last character 

for i in range(len(str3)):
    print(i, " ", str3[i])
    
# Slicing for substrings
# for slicing we use subscript operator
# inside the subscript operator we use (:)
# before or after : an integer is used 

name = "myfile.py" # string

name[:] # entire string

name[0:] # entire string

name[0:1] # first character 

name[0:2] # the first 2 characters

name[:len(name)]  # entire string

name[-3:] # the last three characters 

name[2:6] # extract 'file'

# in operator
# testing for a substring with the in operator

fileNames = ["myfile.py", "first.txt", "resume.pdf", "sort.py"]

for f in fileNames:
    if ".py" in f:
        print(f)

"""
Assume that the variable data refers to the string "myprogram.exe". 
Write the values of the following expressions:
    
Assume that the variable data refers to the string "myprogram.exe". 
Write the expressions that perform the following tasks:
a. Extract the substring "gram" from data.
b. Truncate the extension ".exe" from data.
c. Extract the character at the middle position from data.

Assume that the variable myString refers to a string. 
Write a code segment that uses a loop to print the characters of the string 
in reverse order.

Assume that the variable myString refers to a string, 
and the variable reversedString refers to an empty string. 
Write a loop that adds the characters from myString to reversedString in reverse order.

"""




























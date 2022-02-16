"""
for loop
Why ?
    execute somthing repeatly for a definite no of times
Syntax
=======
for <variable> in range(<an integer expression>):
    <statement-1>
    .
    .
    <statement-n>
"""
# way 1
print("Greetings" * 3)

# way 2 
print("Greetings")
print("Greetings")
print("Greetings")

# print 1 to 100
print(1) # not an efficient way
print("=====")

# range 
x = range(10)
print(x)

# print 1 to 10
for i in range(10): # n-1, starting point is 0 & ends with n-1
    print(i)
    
# achieve 1 to 10
for i in range(1, 11): # starting point is 1 & ends with n-1
    print(i)
    
"""
Write a loop that prints your name 10 times. 
Each output should begin on a new line.
"""
for i in range(10):
    print("joshua")

"""
Write a loop that prints the first 128 ASCII values followed by 
the corresponding characters. Be aware that most of the ASCII values 
in the range “0..31” belong to special control characters with no 
standard print representation, so you might see strange symbols 
in the output for these values.
"""
print(ord('a')) # converting a char to ascii
print(chr(97)) # converting your ascii equ to a char

for x in range(0,129):
    print("ASCII rep: ",ord(chr(x)), "Actual char: ", chr(x))
    
"""
Assume that the variable teststring refers to a string. 
Write a loop that prints each character in this string, 
followed by its ASCII value.
0 1 2 3
b l r k 
"""
teststring = "blrk"
print(len(teststring))

for j in range(len(teststring)):
    print(teststring[j], "ASCII: ", ord(teststring[j]))







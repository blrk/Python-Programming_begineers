"""
testing foirmating 
"""
# withouyt using formatting options
print(1, 100000)
print(10, 100000)
print(100, 100000)

# formating text for output
"""
multiple rows of data / tabular data
data can aligned in columns
either left-justify or right-justify
maintain margin b/w columns 
format a sequence of data values, you have to construct a format 
string that includes a format code for each datum and place the 
data values in a row following the % operator
"""
# syntax 
# <format string> % <datum>
print("one")
print("%6s" % "Five") # right-justify
print("%-6s" % "Four") # left-justify

# try numbers 
print("%10d" % 100000)
print("%10d" % 1000000)
print("%10d" % 10000000)
print("%10d" % 10000000)

# <format string> % (<datum–1>, ..., <datum–n>)

# %<field-width>.<precision>f # floating point number

sal = float(input("enter the salary:"))
print("Salary=$%0.1f" % sal)

x = 100
y = 1000
z = 10000

print("%8d" % x, y, z)

# Homework
"""
Generate a supermarket bill using format string
"""

# while loop 
# syntax
"""
while <condition>:
    <sequence of stements>
"""
# enter a number or enter to quit

sum = 0

data = input("enter a number of press enter to quit:")
while data != "":
    number = int(data)
    sum += number # sum = sum + number
    data = input("enter a number of press enter to quit:")
print("sum is:", sum)

# print a sequence
count = 1
while count <= 10:
    print(count) 
    count +=2

# while of true

sum = 0

while True:
    data = input("Enter a number or just enter to quit:")
    if data == "":
        break
    number = int(data)
    sum += number
print("sum is:", sum)





































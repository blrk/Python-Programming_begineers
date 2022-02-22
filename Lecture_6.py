# While loop 
# syntax
"""
while <condition>:
    <sequence of statement block>
"""
sum = 0
data = input("Enter a number or press enter key to exit:")
while data != "":
    num = int(data)
    sum += num
    data = input("Enter a number or press enter key to exit:")
print("sum is:", sum) 

# count forward
count = 1
while count <= 10:
    print(count)
    count += 1
   
# count down 
count = 10
while count >= 1:
    print(count)
    count -= 1

# loop never ends
# never run this
while True:
    print("hello")
    
s = 0
while True:
    data = input("Enter a number or press enter key to exit:")
    if data == "":
        break
    num = int(data)   
    s += num # s = s + num 
print("sum is:", s)     
"""
AND operation
T T = T
T F = F
F T = F
F F = F

OR 
T T = T
T F = T
F T = T
F F = F

"""

while True:
    num = int(input("Enter a number"))
    if num >= 1 and num <= 10:
        break;
    else:
        print("give a num b/w 1 and 10")
        
"""
The factorial of an integer N is the product of the 
integers between 1 and N, inclusive. 
Write a while loop that computes the 
factorial of a given integer N.

5! = 1 * 2 * 3 * 4 * 5 = 120
"""
n=int(input("Enter a number:"))
num = 1
while n >= 1:
    num *= n
    n -= 1
print("fact:", num)


        












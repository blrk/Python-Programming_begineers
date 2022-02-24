# Ex-2
# Function
# it is a piece of code or block of code 
# code get executed when called 
# return a result back to the caller 

# function defnition 
def fun1(): # function header 
    print("welcome CE") # body of the function
    
fun1() # calling a function, invoke a function

def fun2(x):
    print("exponent of x:", x ** 2)
    
fun2(2)

def fun3(x):
    return(x ** 2)
    
res = fun3(2)
print("exponent of x:", res)

# Abbitrary argumnenbts 

def fun4(*data):
    for i in range(len(data)):
        print(data[i])
    
fun4(1,2,4,5,8, 9, 5)

# Abbitrary keyword arguments

def fun5(**student):
    print(student["regno"])
    
fun5(regno="urk21cs001", name="John", state="TN")

# list 

l1 = [1, 2, 6, 7, 8]

print(l1)
print(l1[2])
l1.append(10)
print(l1)
l1.insert(1, 9)
print(l1)

l2 = ["apple", "orange", "jackfruit"]

l2



















    

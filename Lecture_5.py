# Looping statement 
"""
Write a program that computes an investment report. 

The inputs to this program are the following:
• An initial amount to be invested (a floating-point number)
• A period of years (an integer)
• An interest rate (a percentage expressed as an integer)

The program uses a simplified form of compound interest, 
in which the interest is computed once each year and added 
to the total amount invested.

Print year, startBalance, interest, end balance for every year 

finally, print ending balance and total interest earned 
"""

# get inputs from the user 
startBalance = float(input("enter the amount tobe invested:"))
years = int(input("Enter the number of years:"))
rate = int(input("Enter the rate of interest as % :"))

# convert the rate of interest to a decimal no
rate = rate / 100

# accumlating the interest 
totalInterest = 0.0

# compute and print the results for each year 
print("Years \t startBalance \t interest \t endBalance")
print("---------------------------------------")
for y in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print(y,"\t", startBalance, "\t", interest,"\t", endBalance)
    startBalance = endBalance
    totalInterest += interest
    
# print the final results 
print("---------------------------------------")
print("ending Bal:", endBalance)
print("total interest earned:", totalInterest)
print("---------------------------------------")

# nested looping stements
# create a loop inside another loop
for i in range(5): # outer loop i = 0, 1, 2, 3, 4
    for j in range(5): # inner loop j = 0, 1, 2, 3, 4 j=5? going out of the range 
        print("j:", j)

for i in range(5): # outer loop i = 0, 1, 2, 3, 4
    for j in range(5): # inner loop j = 0, 1, 2, 3, 4 j=5? going out of the range 
        print("i:", i)

for i in range(1, 6): # loop header
    for j in range(1, 6): #  <statements for (i)> 
        print(j, end=" ") # <statements for (j) loop > 
    print("") # next statement of inner loop / block state of outer loop 
# next statment of outer loop 

for i in range(1, 6): # i = 1, j= 1 - 2 i=2 j = 1 - 3
    for j in range(1, i + 1):  
        print(j, end=" ")  
    print("") 
    
for i in range(1, 6): 
    for j in range(1, i + 1):  
        print(i, end=" ")  
    print("") 

for i in range(1, 6): 
    for j in range(1, i + 1):  
        print("*", end=" ")  
    print("") 

# print ABCD 
"""
A
A B
A B C
A B C D
A B C D E

A
B C
D E F
G H I J 
K L M N O
"""



























"""
File: store data
    
Text Files:
    type of a file
    store data
    data can be much larger
    can be given as an input to a pgm
    less chances for error
    data can be used repeatedly
    
Limitations of traditional way of i/p
    errors
    when running the pgm repeatedly-
    everytime we have to type data
    
"""
# Text Files and Their Format
"""
RTF --> Rich text format
text 
numbers etc
"""
# Writing Text to a File
"""
open(p1, p2)
p1 --> filename
p2 --> "mode string" w --> write, output
                     r --> read, input 
                     rw --> read, write
                     a --> append
write(i/p)                
                     
"""
f1 = open("file1.txt", 'w')
f1.write("CSE \n Karunya\n")
f1.close()

# Writing Numbers to a File
f2 = open("file2.txt", 'w')
for i in range(0, 11):
    f2.write(str(i) + "\n")
f2.close()

# Reading Text from a File
f1 = open("file1.txt", 'r')
text = f1.read()
print(text)
f1.close()

f1 = open("file1.txt", 'r')
for line in f1:
    print(line)
f1.close()

f1 = open("file1.txt", 'r')
while True:
    line = f1.readline()
    if line == "":
        break;
    print(line)
f1.close()

# Reading Numbers from a File
f2 = open("file2.txt", 'r')
sum = 0
for line in f2:
    line = line.strip()
    sum += int(line)
print("sum is :", sum)
f2.close()

f2 = open("file2.txt", 'r')
sum = 0
for line in f2:
    wordList = line.split()
    for word in wordList:
        sum += int(word)
print("sum is:", sum)
f2.close()

"""
Write a code segment that opens a file named myfile.txt for input 
and prints the number of lines in the file.

Write a code segment that opens a file for input and 
prints the number of four-letter words in the file.

Assume that a file contains integers separated by newlines. 
Write a code segment that opens the file and prints the 
average value of the integers

Write a code segment that prompts the user for a filename. 
If the file exists, the
program should print its contents on the terminal. 
Otherwise, it should print an
error message.

"""














    


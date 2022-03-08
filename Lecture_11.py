# 97 - 122
"""
Encryption : translating your text into a secret code,
PUrpose : Transfer a text in internetr it is not safe

Caesar cipher: 
    i/p : invaders --> plain text
    o/p : lqydghuv --> chiper text
    
Which decides the alternative alphabet? : key --> integer number (1 to 26)

key = 3

1                                                 26
a  b c d e f g h i j k l m n o p q r s t u v w x y z 
97                                                 122      ASCII

If the input is character ord value is > 122

ord('a')

97 + 3 - (122 - 121 + 1)

= 99

# decryption 
ord('x')

120 

120 + 3 = 123

If the input is character ord value is > 122

122 - 3 - (97 - 97 - 1)

= 120
chr(120)

"""
ord('a')
ord('z')
chr(100)
ord('y')
chr(124)
chr(98)
ord('x')
chr(120)

# encryption

plainText = input("Enter one word (in lowercase): ") #abc
key = int(input("Enter the key: "))

code = "" #cipher text 

for c in plainText:
    ordValue = ord(c)
    cipherValue = ordValue + key
    if cipherValue > ord('z'):
        cipherValue = ord('a') + key - (ord('z') - ordValue + 1)
    code += chr(cipherValue)
print(code)

# decryption

cipherCode = input("Enter one word (in lowercase): ") 
key = int(input("Enter the key: "))

plainText = ""

for c in cipherCode:
    ordValue = ord(c)
    cipherValue = ordValue - key
    if cipherValue < ord('a'):
        cipherValue = ord('z') - key - (ord('a') - ordValue - 1)
    plainText += chr(cipherValue)
print(plainText)













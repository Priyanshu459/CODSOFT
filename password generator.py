i=0
while i==0:
    import random
    import string
    x=int(input("enter the password length , you want to generate  "))
    chars =string.ascii_letters
    chars +=string.digits
    chars +=string.punctuation
    password=""
    for i in range(x):
        next_char = random.choice(chars)
        password +=next_char
        print("your random password generated is ", password)
        i +=1      

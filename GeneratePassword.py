import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(input(f"Number of password generation: \n"))
length = int(input(f"Generated password length: \n"))

for i in range(number):
    password = ""
    for j in range(length):
        password += random.choice(chars)
    print(password)
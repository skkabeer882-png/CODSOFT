import random
import string

# Password Generator Program

print("PASSWORD GENERATOR")

# letters, numbers and symbols
chars = string.ascii_letters + string.digits + string.punctuation

try:
    
    # taking length from user
    size = int(input("Enter password length: "))

    password = ""

    # generating password
    for i in range(size):
        password = password + random.choice(chars)

    # displaying final password
    print("Your Password is:", password)

except:
    
    # if user enters wrong input
    print("Invalid Input")

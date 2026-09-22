import random
import string

print("=== Password Generator ===")

length = int(input("Enter the password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length): # length for password 
    password += random.choice(characters)

print("\nThe Generated Password is:")
print(password) 

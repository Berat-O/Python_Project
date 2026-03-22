import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_+="

try:
    length = int(input("Enter password length: "))
    
    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = ""
        
        for i in range(length):
            char = random.choice(characters)
            password += char
        
        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J',  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to Password Generator")

no_of_letters = int(input("How many letters you want in your password?\n"))
no_of_symbols = int(input("How many symbols you want in your password?\n"))
no_of_numbers = int(input("How many numbers you want in your password?\n"))
password_list = []
for i in range(1, no_of_letters+1):
    char = random.choice(letters)
    password_list += char

for i in range(1, no_of_symbols+1):
    char = random.choice(symbols)
    password_list += char

for i in range(1, no_of_numbers+1):
    char = random.choice(numbers)
    password_list += char

random.shuffle(password_list)

# converting list to string
password = ""
for i in password_list:
    password += i
print("Password =", password)

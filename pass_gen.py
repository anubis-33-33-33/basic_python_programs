import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")

nr_letters = int(input("How many letters would you like to generate? "))
nr_symbols = int(input("How many symbols would you like to generate? "))
nr_numbers = int(input("How many numbers would you like to generate? "))

password_list = []

range(1, 41)
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)


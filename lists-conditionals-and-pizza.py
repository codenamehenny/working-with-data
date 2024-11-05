# working with data
#1. List Comprehensions: Create a list of numbers from 1 to 10, then use a list comprehension to create another list of their squares.
# list of numbers 1-10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# each number squared by iterating over the numbers list
squares = [number**2 for number in numbers]

# print both lists
print(f"Numbers list:", numbers)
print(f"Squares list:", squares)


#2. Conditional Logic:
#Write a Python program that checks if a number is odd or even and
#prints a message based on the result.

# iterating over the exisiting numbers list using the modulus operator to find numbers without remainders
for number in numbers:
    if number%2:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


# 3. Pizza Toppings Program:
#Write a program that asks the user for their favorite pizza toppings,
#append each topping to a list and print all the toppings they entered with a for loop.

print("\nWelcome to the Pizza Toppings Program!")
# empty list ready to add toppings
toppings = []
# entering while loop to be able to take multiple inputs (toppings)
while True:
    topping = input("What are your favorite pizza toppings? (Enter 'exit' when done): ")
    # breaking the while loop once user enters exit
    if topping.lower() == 'exit': # making input case insensitive
        break
    # adding topping to the toppings list
    toppings.append(topping)
    print(f"{topping} added successfully")
# printing all toppings in the list using a for loop
print("Here's the list of your favorite toppings:")
for topping in toppings:
    print(topping)


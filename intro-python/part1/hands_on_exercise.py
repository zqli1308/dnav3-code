"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("type=",type(pi),"vlaue=",pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print("i < 50")
else:
    print("i > 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit=='orange':
    print("color is orange")
elif picked_fruit=='strawberry':
    print("color is red")
elif picked_fruit=='banana':
    print("color is yellow")



# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def muxtwo_number(number_1,Number_2):
    The_result=number_1*Number_2
    return The_result

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",muxtwo_number(12,96))

print("48 x 17 =",muxtwo_number(48,17))

print("196523 x 87323 =",muxtwo_number(196523,87323))

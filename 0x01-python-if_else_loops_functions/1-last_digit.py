#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
if number > 0 or number == 0:
    lastdigit = number % 10
if number < 0:
    lastdigit = -1 * (abs(number) % 10)
if lastdigit > 5:
    print(f"{str1} {number} is {lastdigit} and is greater than 5")
if lastdigit == 0:
    print(f"{str1} {number} is {lastdigit} and is 0")
if lastdigit < 6 and lastdigit != 0:
    print(f"{str1} {number} is {lastdigit} and is less than 6 and not 0")

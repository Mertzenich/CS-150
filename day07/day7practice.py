#!/usr/bin/env python3
"""
# Problem 1
for x in range(11):
    print(x)


# Problem 2
sum = 0
for x in range(11):
    sum += x
print(sum)


# Problem 3
# posNum = int(input("Enter a positive (+) number: "))
posNum = 3
for x in range(12):
    print(posNum*x)


# Problem 4
factorial = int(input("Enter number to find factorial: "))
times = factorial

while times != 1:
    times -= 1
    factorial = factorial * times
print(factorial)

# Problem 5
numberOne = int(input("Enter first number: "))
numberTwo = int(input("Enter second number: "))
powered = numberOne ** numberTwo
print(powered)


# Problem 6
def evenSum(num1, num2, num3, num4, num5):
    result = 0
    ls = (num1, num2, num3, num4, num5)
    for x in ls:
        if x%2 == 0:
            result += x
    return result

print(evenSum(4, 5, 6, 2, 7))


# Problem 7
def primeChecker(proposition):
    # Check from 2 to n-1
    for x in range(2, proposition):
        if (proposition % x == 0):
            return False
    return True

posInt = int(input("Enter a positive integer: "))

print(primeChecker(posInt))


# Problem 8

while True:
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    print(num1+num2)
    cont = input("Would you like to continue? Y/n ")
    if cont == '':
        continue
    elif cont.lower() == 'y':
        continue
    elif cont.lower() == 'n':
        break
    else:
        print('Invalid input')
        continue

# Problem 9
print('Enter as many numbers as you want, when done enter 0000')
highest = 0
lowest = 0
while True:
    a = int(input('#: '))
    if a == 0000:
        break
    else:
        if a > highest:
            highest = a
        elif a < lowest:
            lowest = a
        else:
            continue

print(highest, lowest)

"""

many = int(input("How many in series? "))

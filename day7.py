#!/usr/bin/env python3

# Part A

intList = []  # Empty list

for x in range(3):
    enter = int(input('Enter integer ' + str(x+1) + ' '))  # Take integer as input
    intList.append(enter)  # Add input integer to end of list

maxVal = 0

for x in intList:
    if x > maxVal:  # Check if current item in list is higher than the current maximum
        maxVal = x  # If the value is bigger than the current maximum set maxVal to the larger one.
    else:
        continue    # Continue iterating through list.

print(maxVal)  # Prints max value from the inputted intList


# Part B

forward = int(input('Enter integer to be reversed: '))

items = []

for x in str(forward):  # Loop to add each character from the forward input to the items list.
    items.append(x)

items.reverse()         # Reverse the list

result = ''

for x in items:         # Put reversed list into the result string
    result += str(x)

print(result)           # Print the reversed string

# Part B In Class Solution
forward2 = int(input('Enter integer to reverse: '))
x = forward2 % 10
reverse = reverse*10 + x

# Part C

donationCount = int(input('How many donations are you collection? '))
sum = 0

for i in range(donationCount):  # Get input as many times as there were donations
    sum += int(input('How much is donation #' + str(i+1) + " in dollars? "))  # Add the donation amount to the sum.

print("You have collected a total of $" + str(sum) + ".")  # Print the sum of all donations


# Part D

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

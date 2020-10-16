import random

# Problem 1
# already was done on day 5
"""
# Calculation Functions
def add(num1, num2): # Addition
    answer = num1 + num2
    return answer

def sub(num1, num2): # Subtraction
    answer = num1 - num2
    return answer

def mult(num1, num2): # Multiplication
    answer = num1 * num2
    return answer


def div(num1, num2): # Division
    answer = num1 / num2
    return answer

def sqrt(num): # Square Root
    answer = num ** 0.5
    return answer

def pwr(num1, num2): # Power
    answer = num1 ** num2
    return answer

def modulus(num1, num2): # Modulo
    answer = num1 % num2
    return answer

# Get input and run the appropriate function.
def problem():
    problemType = int(input("Do you want to:\nAdd[1], Subtract[2], Multiply[3], Divide[4], SQRT[5], Power[6], or Modulus[7]?\n"))
    if problemType == 1 or 2 or 3 or 4 or 6 or 7:
        value1 = float(input("Enter your first value: "))
        value2 = float(input("Enter your second value: "))
        if problemType == 1:
            result = add(value1, value2)
        if problemType == 2:
            result = sub(value1, value2)
        if problemType == 3:
            result = mult(value1, value2)
        if problemType == 4:
            result = div(value1, value2)
        if problemType == 6:
            result = pwr(value1, value2)
        if problemType == 7:
            result = modulus(value1, value2)
        return result
    elif problemType == 5:
        value = input("Enter your value: ")
        result = sqrt(value)
        return result
    else:
        return "Did not select appropriate problem type."

print(problem()) # Function Call
"""

def luggage(weight):
    if weight <= 40:
        return 'None'
    else:
        charge = str((weight-40)*2)
        return '$' + charge

print('Charge:', luggage(41))

def clothing(temp):
    if temp >= 70:
        return 'Shorts'
    else:
        return 'Pants'
    
print(clothing(69))

def tempConvert(temp, type):
    if type == 'C':
        F = (temp * 9 / 5) + 32
        return F
    elif type == 'F':
        C = (temp - 32) * 5/9
        return C

print((tempConvert(32, 'F')))

def guessCheck(guess, start, stop):
    randomNumber = random.randrange(start, stop)
    if guess == randomNumber:
        return 'Correct!'
    else:
        return 'Wrong!'

print(guessCheck(5,0,10))
#print(guessCheck(input('Enter a number: '), 0, 10))


balance = 2500


def pin():
    pin = 4771
    num = int(input('Enter your PIN: '))
    if num == pin:
        return True
    else:
        return False


def deposit(amount):
    global balance
    balance += amount
    return balance


def withdraw(amount):
    global balance
    balance -= amount
    return balance


def checkBalance():
    global balance
    return balance

def prompt():
    global verify
    command = input('\nOptions:\nDeposit\nWithdraw\nCheck\nLogout\n\nWhat would you like to do? ')
    if command == 'Deposit':
        result = deposit(float(input('How much would you like to deposit? ')))
        return result
    elif command == 'Withdraw':
        result = withdraw(float(input('How much would you like to withdraw? ')))
        return result
    elif command == 'Check':
        return checkBalance()
    elif command == 'Logout':
        verify = ''
        return 'You have been logged out.'
        

verify = ''

def ATM():
    global verify

    if verify == False:
        return 'Verification failed!'
    elif verify == '':
        verify = pin()
    elif verify == True:
        return prompt()
    
        
while True:
    ATM()
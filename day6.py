# Assignment 6
# by Adam Mertzenich


# Problem 1
X = float(input('Enter first number: '))
Y = float(input('Enter second number: '))
Z = float(input('Enter third number: '))

if X <= Y <= Z:
    x = X
    y = Y
    z = Z

elif X >= Y >= Z:
    x = Z
    y = Y
    z = X

elif X <= Y >= Z:
    if X >= Z:
        x = Z
        y = X
        z = Y
    if X <= Z:
        x = X
        y = Z
        z = Y

elif X >= Y <= Z:
    if X >= Z:
        x = Y
        y = Z
        z = X
    if X <= Z:
        x = Y
        y = X
        z = Z

print(x,y,z)


# Problem 2
d1 = int(input('D1: '))
d2 = int(input('D2: '))
output = d1+d2
winners = (7,11)
losers = (2,3,12)

if d1 > 6 or d2 > 6 or d1 < 1 or d2 < 1:
    print('Out of range')
else:
    if output in winners:
        print('Winner!')
    elif output in losers:
        print('Loser!')
    else:
        print('Points:', output)

# Problem 3
hoursWorked = float(input('Hours Worked: '))
wage = float(input('Wage: '))

if hoursWorked <= 40:
    print('Pay: ', hoursWorked*wage)
else:
    OT = hoursWorked-40
    pre = 40*wage
    OTPay = OT * (wage*1.5)
    print('Pay + OT: ', pre + OTPay)
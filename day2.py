# Assignment no. 2
# Submitted by Adam Mertzenich

# Problem 1
print('Problem 1:')
age = input('Please enter your age: ') # Take age as input
ageDays = age*365 # Convert the age from years into days
print('You are ' + str(ageDays) + ' days old.\n') # Print the days

# Problem 2
# Add parenthesis to the expression 10 * 9 - 9 to change its value from 81 to 0.
# 10*9-9
# Answer: (10*9)-9
print('Prolem 2:')
print('(10*9)-9 = ' + str((10*9)-9) + '\n')

# Problem 3
print('Problem 3')

principal = 250.0
rate = 0.05
compounded = 1.0
years = 3.0

A = principal * ((1+rate/compounded)**(compounded*years))
print(A)

# Ask user for input
principal = float(input('Principal Amount (Initial Investment): '))
rate = float(input('Annual Nominal Interest Rate (Decimal): '))
compounded = float(input('Number of times the interest is compounded per year: '))
years = float(input('Number of years: '))
result = principal * ((1+rate/compounded)**(compounded*years))

print('Result: ' + str(result)) # Print result of user input

print('Rounded:' + str(round(result, 2))) # Round the result to 2 decimals. 


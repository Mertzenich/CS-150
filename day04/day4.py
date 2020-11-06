# Assignment 4
# Submitted by Adam Mertzenich

import math

# Problem 1
def apply(val): # Returns casted as a float
    return(float(val))

def worker(principal, rate, compounded, years): # Takes p,r,c,y values and applies the formula
    A = apply(principal) * ((1+apply(rate)/apply(compounded))**(apply(compounded)*apply(years)))
    print(A)

def grabber(): # Gets user input and passes values to the worker function
    principal = input('Principal Amount (Initial Investment): ')
    rate = input('Annual Nominal Interest Rate (Decimal): ')
    compounded = input('Number of times the interest is compounded per year: ')
    years = input('Number of years: ')
    worker(principal, rate, compounded, years)


grabber() # Run

# Problem 2
def sphere_volume(r):
    return 4/3*math.pi*float(r)**3

print(sphere_volume(input('Please enter the radius of your sphere: ')))
# Q: Should the print statement go in the sphere_volume function or the main program?
# A: I think the print statement should be outside the function because you might want to later use the function without printing the information. For example you might run a calculation using the volume of the sphere and only need to print the end result.

# Problem 3
def remainderDivmod(divisor, dividend):
    return divmod(divisor, dividend)[1] # Since we were tasked to calculate the remainder I only return the second item in the array which contains the remainder.

def remainderModulus(divisor, dividend):
    return divisor % dividend

print('Remainder Using divmod: ', remainderDivmod(3, 75))
print('Remainder using modulo: ', remainderModulus(3, 75))
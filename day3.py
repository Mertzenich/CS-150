# Problem 1
h = float(input("Please enter the height of the triangle: "))
b = float(input("Please enter the base of the triangle: "))
area = (h * b) /2
print("Triangle Area: " + str(area))

# Problem 2
a = float(input("Enter \'a\' value: "))
b = float(input("Enter \'b\' value: "))
c = float(input("Enter \'c\' value: "))

answer1 = a**2 + b**2 + c**2 + 2*a*b + 2*b*c + 2*c*a
print(answer1)
answer2 = a**3 + 3*a**2*b + 3*a*b**2 + b**3
print(answer2)


# Extra Problem
float1 = float(input('Enter first number: '))
float2 = float(input('Enter second number: '))
float3 = float(input('Enter third number: '))
sum = float1+float2+float3
print(sum)

guest = input('What is your name? ')
print('Salutations, how are you doing, ' + guest + '?')


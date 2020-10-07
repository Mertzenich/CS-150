pie = 3.14
radius = 5
area = 2*pie*radius*2
print("The area of the circle is = ",area)
circumference = 2*(pie)*(radius)
print("The circumference of the circle is = ",circumference)

print("\n\n~~~~~~~~~~~~~~~\n\n")

number = int(input("please enter the number to get its square ,square root ,cube, cube root: "))
print(" The square of ",number , "     = " ,number*number,
      "\n The squareroot of ",number , " = " ,number**1/2 ,
      "\n The cube of ",number , "       = " ,number*number*number,
      "\n The cuberoot of ",number , "   = " ,number**1/3)


print("\n\n~~~~~~~~~~~~~~~\n\n")

number_second = int(input("Please enter the number to see if its an even number or not: "))

if number_second%2 == 0:
    result = 'even'
if number_second%2 == 1:
    result = 'odd'
print ("The result is", result + '.')

# calculator.py

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


def modulus(num1, num2):  # Modulo
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

print(problem())  # Function Call

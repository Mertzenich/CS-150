#!/usr/bin/env python3

# Problem 1
def palCheck(w):
    if w == w[len(w)::-1]:
        return True
    return False

palindrome = "madam"

print(palCheck(palindrome))


# Problem 2

def firstResult(s):
    result = s[0] + s[1:].replace(s[0], '$')
    return result

# Expected Result: "resta$t"
print(firstResult("restart"))


# Problem 3
ID = input('ENTER ID: ')
PWD = input('ENTER PASS:')
for i in PWD:
    PWD = PWD.replace(i, '*')

print(f'Your ID: {ID}@example.com')
print(f'Your PWD: {PWD}')


# Problem 4

def vowCount(s):
    count = 0
    count += s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')# sometimes y + s.count('y')
    return count

word = input()
print(vowCount(word))

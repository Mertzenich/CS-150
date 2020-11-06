#!/usr/bin/env python3
"""
name = "Adam"
for letter in name:
    print(letter)

print()

names = ["Adam", "Joseph", "Mary"]
for name in names:
    print(name)

print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        #break
        continue
    print(x)

for num in range(6):
    print(num)
    #print("Hello", num)

print()


for num in range(2):
    print(num)

print()

for num in range(1, 4):
    print(num)

print()

for num in range(2, 20, 2):
    print(num)

print()
sum = 0

for num in range(1, 11):
    sum = sum+num
    print(num)


print(sum)
"""
print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

num = 1

while True:
    if num < 11:
        print(2*num)
        num += 1
    else:
        break

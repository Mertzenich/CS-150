#!/usr/bin/env python3

        # Name, age, year, hometown
pInfo = [
    ['Name', 'Adam'],
    ['Age', 20],
    ['School' 'Freshman'],
    ['Hometown', 'Decorah']
]
print(pInfo)
print(len(pInfo))
print(pInfo[0][1])

print(pInfo[1::2])

for i in pInfo:
    print(i)

mult = pInfo[1][1]
n = 1
while n < 10:
    print(mult*n)
    n+=1

def attendance():
    result = []
    done = ''
    while done.lower() != 'y':
        result.append(input('Enter name: '))
        print(result)
        done = input('Are you done? y/N ')
    return result

myList = [item for item in range(6)]
yourList = [item ** 2 for item in myList]
print(yourList[1:])

testlist = [item for item in range(11) if item % 2 == 0]
print(testlist)

#print(attendance())

n = '45, 50, 49, 46, 41'
wds = n.split(', ')
print(wds)

sum = 0
for i in wds:
    sum = sum + int(i)

print(sum)

print(" ".join(wds))
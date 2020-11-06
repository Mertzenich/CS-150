#!/usr/bin/env python3

# Problem 1
file_ref = open('qbdata.txt', 'r')
lineCount = int(input('How many lines do you want to see? '))
for i in range(lineCount):
    print(file_ref.readline())
file_ref.close()


# Problem 2
file_ref = open('qbdata.txt', 'r')
ls = []
for i in file_ref:
    ls.append(i)
print(ls[-10:])
file_ref.close()


# Problem 3
file_ref = open('qbdata.txt', 'r')
print(len(file_ref.readlines()))
file_ref.close()


# Problem 4
file_ref = open('qbdata.txt', 'r')
print(len(file_ref.read().split()))
file_ref.close()


# Problem 5
file_ref = open('qbdata.txt', 'r')
new_file = open('newfile.txt', 'w')
for line in file_ref:
    data_list = line.split()
    print(data_list[0].upper(), data_list[1].upper(), data_list[10]) # Did not know which number was the rating so i assume it was this one.
    new_file.write(data_list[0].upper() + ' ' + data_list[1].upper() + ' ' + data_list[10] + '\n')
new_file.close()
file_ref.close()

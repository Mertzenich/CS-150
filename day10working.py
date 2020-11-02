#!/usr/bin/env python3

file_ref = open('qbdata.txt', 'r')

# for line in file_ref:
#     print(line)
#     data_list = line.split()
#     print(data_list[0], data_list[1])

line = file_ref.readlines()
print(line)

file_ref.close()

# with open('qbdata.txt') as md:
#     print(md)#it prints the name, mode and encoding
#     for line in md:
#         print(line)

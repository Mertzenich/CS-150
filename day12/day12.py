#!/usr/bin/env python3
# 1. Write a program that reads a qbdata file . and make a dictionary for each player.
# Name f each dictionary should be the first name of that player .
# Save all the dictionary name in a list .
# • The keys of the dictionary are:
# (First Name, Last Name, Position, Team, Completions, Attempts, Yards, TDs, Ints, Comp%, Rating)


try:
    file_ref = open('qbdata.txt', 'r')

    data = {}

    for line in file_ref:
        split = line.split()
        data[split[0]] = line.split()

    file_ref.close()

    print(data['Alx'])
except KeyError:
    print('That name is not in the qbdata.txt')

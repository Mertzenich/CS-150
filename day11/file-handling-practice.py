#!/usr/bin/env python3

import datetime

current_date = datetime.datetime.now()
current_day = current_date.day
current_month = current_date.month
current_year = current_date.year
date = str(current_day) + '-' + str(current_month) + '-' + str(current_year)

names = []
while True:
    new_name = input('Enter name: ')
    if new_name == 'done':
        break
    else:
        names.append(new_name)



file_ref = open('attend.txt', 'a')


file_ref.write(date + '\n')
for i in names:
    file_ref.write(str(i) + '\n')

file_ref.close()

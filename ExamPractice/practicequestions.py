#!/usr/bin/env python3

import datetime
# import tkinter as tk
# from tkinter import ttk, messagebox, simpledialog, filedialog


# current_date = datetime.datetime.now()

# # Problem 1

# odd = []
# even = []
# for i in range(1,101,2):
#     odd.append(i)
# for i in range(2,101,2):
#     even.append(i)


# # Problem 2

# str_list = []
# int_list = []
# float_list = []

# big_list = ['test', 6, 7, 'another', 3.14, 5, 1.6, 'final']
# for i in big_list:
#     if type(i) == str:
#         str_list.append(i)
#     elif type(i) == float:
#         float_list.append(i)
#     elif type(i) == int:
#         int_list.append(i)
#     else:
#         continue

# # Problem 3

# x_list = [6,4,7,2,3,8,11,9]
# x_list.sort()
# x_list = [7,3,6,9,3,8,2,6,8,9,10]
# x_list.sort()

# # Problem 4

# logIns = {'Jim': 'abc123', 'Tracey': 'ghi456', 'Allen': 'lmn789'}

# accounts = {
#     'Jim': {'accountNum': 11111, 'balance': 4000, 'lastLogIn': '11/15/2020'},
#     'Tracey': {'accountNum': 11112, 'balance': 4500, 'lastLogIn': '11/05/2020'},
#     'Allen': {'accountNum': 11113, 'balance': 2000, 'lastLogIn': '10/15/2020'}
# }
# print(accounts)

# loginPrompt = input('Enter Username: ')
# passPrompt = input('Enter Password: ')
# if loginPrompt in logIns:
#     if logIns[loginPrompt] == passPrompt:
#         print('\nLog in successful.')
#         print(f'Account Number: {accounts[loginPrompt]["accountNum"]}')
#         print(f'Balance: {accounts[loginPrompt]["balance"]}')
#         print(f'Last Login: {accounts[loginPrompt]["lastLogIn"]}')
#         accounts[loginPrompt]['lastLogIn'] = f'{current_date}'
#     else:
#         print('\nLog in not successful.')
# else:
#     print('Log in not successful.')


# # Problem 5

# def newAccount(username, balance, accountNum):
#     accounts[username] = {'accountNum': accountNum, 'balance': balance, 'lastLogIn': f'{current_date}'}
# newAccount('Adam', 3295, 11114)


# # Problem 6

# list_1 = ['ava', 'ella', 'linn', 'ava']
# list_2 = ['ella', 'sam', 'laura', 'linn']
# common_list = []
# for i in list_1:
#     if i in list_2:
#         common_list.append(i)
#     else:
#         continue


# # Problem 7

# messagebox.showwarning('Low Battery', 'Change your battery or switch to outlet power immediately')

# # Problem 8
# name = simpledialog.askstring('Input', 'Enter name: ')
# print(name)

# # Problem 9

# initial_string = 'mississippi and arkansas'
# new_string = ''
# for i in enumerate(initial_string):
#     if i[0] % 2 == 0:
#         new_string += i[1].upper()
#     else:
#         new_string += i[1]

# Problem 10

def group_by_owners(files):
    new_dict = {}
    ls = []
    for x in files:
        value = files[x]
        if value not in new_dict:
            new_dict[value] = x
        else:
            ls.append(x)
            new_dict[value] = x

    return new_dict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))

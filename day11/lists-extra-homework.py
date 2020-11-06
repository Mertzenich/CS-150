#!/usr/bin/env python3

cast = ['Amy Adams', 'Jeremy Renner', 'Forest Whitaker', 'Mark O\'Brien', 'Tzi Ma', 'Abigail Pniowsky', 'Julia Scarlett', 'Jadyn Malone']


def add_p():
    query = input('Who would you like to add to the list? ')
    cast.append(query)
    return f'{query} added to the list.'

def del_p():
    query = input('Who would you like to remove from the list? ')
    if query in cast:
        cast.remove(query)
        return f'{query} removed from the list.'
    else:
        return f'{query} not in cast so they can\'t be removed'

def search_p():
    cast_query = input('Which actor/actress do you want to search for? ')
    if cast_query in cast:
        return f'Yes, {cast_query} is in the movie.'
    else:
        return f'No, {cast_query} is not in the movie.'



enter = 1
result = ''
while enter != 5:
    print('''
    Please select one of the following menu options:\n
    1. Add a person to the movie list.\n
    2. Delete a person from the movie list.\n
    3. Search for a person in the movie list.\n
    4. Print out all people currently going to the movie.\n
    5. Close the list.
    ''')

    if result != None or result != '':
        print(result)
        result = ''
    enter = int(input('> '))
    if enter == 1:
        result = add_p()
    elif enter == 2:
        result = del_p()
    elif enter == 3:
        result = search_p()
    elif enter == 4:
        result = 'Cast:\n'
        for i in cast:
            result += i
            result += '\n'
    else:
        continue

class_count = input('How many students are in your class? ')
names = []
for i in range(int(class_count)):
    names.append(input('Please enter their names, one per line. '))
names.sort()
print(names)

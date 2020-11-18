#!/usr/bin/env python3

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525}
print(inventory)
inventory['pears'] = 217
print(inventory)
inventory['apples'] = inventory['apples'] - 5
print(inventory)
print(inventory.keys())
print(inventory.values())
print(inventory.items())
print(inventory.get('apples'))
print()


for i in inventory.values():
    print(i)

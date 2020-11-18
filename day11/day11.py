#!/usr/bin/env python3

# Problem 1 & 2
inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'], 'backpack': ['xylophone','dagger', 'bedroll','bread loaf']}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print(inventory)


# Problem 3
prices = {'banana': 4, 'apple': 2, 'orange': 1.5, 'pear': 3}
stock = {'banana': 6, 'apple': 0, 'orange': 32, 'pear': 15}

for i in prices.keys():
    print(i.capitalize(), '\nPrice:', prices[i], '\nStock:', stock[i])

total = 0
for i in prices:
    total += (prices[i] * stock[i])
print(total)

a = [1, 2, 3]

for item in a.copy():
    if item != 0:
        a.remove(item)
        print('item =', item, 'a =', a)




my_cats = []
while True:
    print(f'Add cat {len(my_cats) + 1} to the list')
    name = input('>')
    if not bool(name):
        break
    else:
        my_cats += [name]

print('Your cat names')
for names in my_cats:
    print('' + names)

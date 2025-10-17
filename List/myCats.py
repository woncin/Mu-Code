my_pets = ['zophie', 'pooka', 'furry']
print('Enter a pet name:')
name = input().strip().lower()
if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    num_of_item = 0
    for key, value in inventory.items():
        num_of_item += value
        print(f'{value} {key}')
    print(f'Total number of items: {num_of_item}')


display_inventory(stuff)


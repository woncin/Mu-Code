
def calculate(val_1, operator, val_2):
    if operator not in ('+', '-', '*', '/'):
        print('Unsupported operator')
    elif operator == '+':
        print(val_1 + val_2)
    elif operator == '-':
        print(val_1 - val_2)
    elif operator == '*':
        print(val_1 * val_2)
    elif operator == '/':
        print(val_1 / val_2)

print('Add, subtract, multiply and divide')
val_1 = int(input('>'))
operator = input('>')
val_2 = int(input('>'))
calculate(val_1, operator, val_2)

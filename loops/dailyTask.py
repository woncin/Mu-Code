daily_tasks = []
while True:
    print(f'Add task {len(daily_tasks) + 1}')
    task = input('>')
    if task == '':
        break
    else:
        daily_tasks += [task]

print('Your daily Task')
count = 0
for task in daily_tasks:
    count += 1
    print(f'{count}. {task}')


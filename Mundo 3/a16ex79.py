list = list()

confirm = '.'
while True:
    if confirm in 'Nn':
        break

    number = int(input('Digit a value: '))
    if number not in list:
        list.append(number)
    else:
        print('this value has already been entered.')

    confirm = str(input('Do you want to continue [Y/N]: '))[0]

    if confirm in 'YyNn':
        if confirm in 'Nn':
            break
    else:
        while confirm not in 'YyNn':
            print('Select a option true.')
            print('-='*20)
            confirm = str(input('Do you want to continue [Y/N]: '))[0]


list.sort()
print('=-'*20)
print(f'you typed: {list}')
# No difficulty. 17/03/23
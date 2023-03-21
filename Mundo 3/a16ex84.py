# important variables.
people = list()
data = list()
weight = list()
record = 0

# loop until stop.
while True:

    # adding weight and name to lists.
    data.append(str(input('name: ')))
    data.append(float(input('weight: ')))
    people.append(data[:])
    data.clear()
    record += 1

    # for continue.
    confirm = str(input('do you want to continue [Y/N]: ')).strip()[0]
    if confirm in 'YyNn':
        if confirm in 'Nn':
            break
    else:
        print('in the next enter between yes or no ;)')

# check the highest and lowest weight.
for person in people:
    int(person[1])
    weight.append(person[1])

# print the final result.
print(f'you registered {record} people\nthe highest weight is {max(weight)} and lowest is {min(weight)}.')

# my way of doing this lesson ( something is missing ). 20/03/23
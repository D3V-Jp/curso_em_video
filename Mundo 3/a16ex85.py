# important variable.
list = [[] for _ in range(3)]

# main function.
for count in range(1,8):
    num = int(input(f'{count}º number: '))
    list[0].append(num)

    # check even and odd.
    if num % 2 == 0:
        list[1].append(num)
    else:
        list[2].append(num)

# call print.
print('=-'*20)
print(f'you input {len(list[0])} numbers\nwhere {list[1]} is even and {list[2]} is odd.')
print('=-'*20)

# easy. 20/03/23
words = ( 'Shaggy','World','Null','Blue','Cat','Dog','Ant Man','Trump','Cicle','Sicko' )

for l in words:
    print(f'\nin the words {l.upper()} have', end=' ')
    for letters in l:
        if letters in 'aeiou':
            print(f'[{letters}]', end=' ')
# I didn't find this lesson difficult.
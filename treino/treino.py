# current year in a variable
from datetime import datetime
current_year = datetime.now().year


while True:

    # check if age is numeric
    print('=-'*20)
    year_birthday = input('year of your birthday: ')
    if not year_birthday.isnumeric():
        print('=-'*20)
        print('do not use space or letters.\ntry again.')
        continue
    year_birthday = int(year_birthday)

    # variable for 100 years and print.
    lastyear = ( year_birthday - current_year ) + 100 + current_year
    print(f'{lastyear} you turn 100 years.')
    
    # if for continue
    print('=-'*20)
    again = input('do you want to continue [Y/N]: ').lower().strip()[0]
    if again in 'yn':
        if again in 'n':
            break
    else:
        print('Option invalid..')
        break

nasc = int(input('Qual sua idade?: '))

if nasc <= 9:
    print('Você será classificado para a categoria MIRIM!')
elif nasc <= 14 and nasc > 9:
    print('Você será classificado para a categoria INFANTIL!')
elif nasc <= 19 and nasc > 14:
    print('Você será classificado para a categoria JUNIOR!')
elif nasc <= 24 and nasc > 19:
    print('Você foi classificado para a categoria SENIOR!')
else: print('Você foi classificado para a categoria MASTER!')

#Achei facil até graças ao AND. 24/02/2023
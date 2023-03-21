count = ( 'zero','um','dois','tres','quatro','cinco',
         'seis','sete','oito','nove','dez','onze',
         'doze','treze','quartoze','quinze','dezesseis',
         'dezessete','dezoito','dezenove','vinte')

while True:
    n1 = int(input('Qual numero você deseja escolher: '))
    n1 = abs(n1)

    if n1 <= 20:
        print(f'O numero escolhido foi {count[n1]}')
        break
    else:
        n1 = int(input('O numero tem que ir de 1 - 20: '))
# Facil. 15/03/23
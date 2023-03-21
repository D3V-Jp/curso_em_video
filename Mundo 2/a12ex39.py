nome = str(input('Qual seu nome?: ')).title()
nasc = int(input('Qual o ano de seu nascimento?: '))
min = 2023 - nasc
falta = (min - 18).__abs__()

if min == 18:
    print('{}, Está na hora de se alistar pro exercito'.format(nome))
elif min >= 18:
    print('{}, Faz {} anos que você deveria ter se alistado, corra para um batalhão próximo e se aliste.'.format(nome,falta))
else: print('Você precisa ter 18 anos para se alistar no exercito e ainda lhe falta {} anos'.format(falta))
print(min)

#Foi a atividade que me senti mais seguro, e mais gostei de fazer até o momento. 23/02/23
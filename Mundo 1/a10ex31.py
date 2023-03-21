d = float(input('Você pretende viajar por quantos KM > '))
p1 = d*0.50
p2 = d*0.45

if d >= 200:
    print('Sua viagem vai sair no valor de R${:.2f}'.format(p2))
else: print('Sua viagem vai sair no valor de R${:.2f}'.format(p1))
# low diff. pouco processamento lógico. 08-07-2022
s = float(input('Qual é seu salário atual? > '))
a1 = s*1.10
a2 = s*1.15
print('='*18)
print('.. CALCULANDO ..')
print('='*18)
if s >= 1250.00:
    print('Seu salário recebeu um aumento de 10 porcento.')
    print('='*18)
    print('Salario atual: R${:.2f}'.format(a1))
    print('='*18)
if s <= 1250.00:
    print('Seu salário recebeu um aumento de 15 porcento')
    print('='*18)
    print('Salario atual: R${:.2f}'.format(a2))
    print('='*18)
# Low diff. 08-07-2022
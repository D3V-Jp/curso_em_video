sexo = input('Qual seu sexo [M/F]: ').strip().upper()[0]
while True:
    if sexo in 'MmFf':
        print('Muito Obrigado, Foi registrado seu sexo!')
        break
    else: 
        sexo = input('Por favor selecione uma opçao valida entre [M/F]: ').strip().upper()[0]
# Tinha como ter feito usando While sexo not in 'MmFf': , eu economizaria umas 5 linhas, porém foi facil. 09/03/23
a = int(input('Qual ano você pretende calcular se é bissexto? > '))
b = a%2

if b == 0:
    print('O ano de {} é bissexto'.format(a))
else: print('O ano solicitado não é bissexto!')
# low diff. usei a lógica do a10ex30. 08-07-2022
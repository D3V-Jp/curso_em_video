print('\033[4;35mLoja Baratão.\033[m')

valores = []
maior_valor = ''
menor_valor = ''

while True:
    produto = str(input('Produto: ')).strip()
    valor = int(input('Valor: '))
    valores += [valor]

    if valor >= max(valores):
        maior_valor = produto
    else:
        menor_valor = produto


    while True:
        confirm = str(input('Deseja continuar: ')).lower().strip()[:3]
        escolhas = ['sim', 'nao']

        if confirm in escolhas:
            break
    if confirm == 'nao':
        break
    else:
        continue

print(f'O item mais caro foi {maior_valor} custando R${max(valores)}.\n O item mais barato foi {menor_valor} custando R${min(valores)}.')
# Não achei dificil. 14/03/23
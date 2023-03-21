from random import randint

produto = randint(1,180)
print('''VALOR DA COMPRA: {:.2f}
    '''.format(produto))

pagamento = int(input('''QUAL A FORMA DE PAGAMENTO: 
[1] DINHEIRO
[2] CARTÃO DEBITO/CREDITO
[3] CARTÃO PARCELADO 2X
[4] CARTÃO PARCELADO 3x ( ou mais )
: '''))

if pagamento <= 4:
    if pagamento == 1:
        print('''
        VALOR DO PRODUTO: R${:.2f}
        VALOR DO DESCONTO: R${:.2f}
        VALOR C/DESCONTO: R${:.2f} '''.format(produto, produto*0.1, produto*0.9 ))
    elif pagamento == 2:
        print('''
        VALOR DO PRODUTO: R${:.2f}
        VALOR DO DESCONTO: R${:.2f}
        VALOR C/DESCONTO: R${:.2f} '''.format(produto, produto*0.05, produto*0.95 ))
    elif pagamento == 3:
        print('''
        VALOR DO PRODUTO: R${:.2f}
        JUROS P/PARCELADO: --
        VALOR DO DESCONTO: R$ --
        VALOR P/PARCELADO: R${:.2f} '''.format(produto, produto, produto ))
    elif pagamento == 4:
        print('''
        VALOR DO PRODUTO: R${:.2f}
        JUROS P/PARCELADO: 20%
        VALOR DO DESCONTO: R$ --
        VALOR COM JUROS: R${:.2f} '''.format(produto, produto*1.20))
else: print('Por favor seleciona uma das opções listadas!')
#Achei legal de fazer, não foi dificil. 25/02/23
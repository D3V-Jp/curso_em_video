casa = float(input('Qual o valor da casa que deseja financiar? > '))
salario = float(input('Qual o valor do seu salário? > '))
parcelas = int(input('Planeja financiar em quantos anos a casa? > '))
valor_parcelas = casa / (parcelas*12)
minimo = salario*0.3

if salario >= minimo:
    print('Você tem condições de fazer esse financiamento portanto, seu emprestimo foi APROVADO!')
else: print('Infelizmente você nao tem condições de fazer esse financiamente portando seu emprestimo foi REPROVADO!')
#Lição concluida em 22/02/23 ( medium diff ) exigiu ajuda.
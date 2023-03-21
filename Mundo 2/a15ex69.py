import random

maioridade = 0
menoridade = 0
masc = 0
fem = 0
femmaior = 0
sex = ['M','F']

count = 0
while count <= 100:
    age = random.randint(0,100)
    sexrandom = random.choice(sex)

    if age >= 18:
        maioridade += 1
    else:
        menoridade += 1
    
    if (sexrandom in 'Ff' and age >= 20):
        femmaior += 1

    if sexrandom in 'Mm':
        masc += 1
    elif sexrandom in 'Ff':
        fem += 1

    count += 1
    
print(f'Tivemos {maioridade} pessoas maior de idade e {menoridade} menor de idade. ')
print(f'Ao todo temos {masc} homens cadastrados e {fem} mulheres cadastradas.')
print(f'Temos {femmaior} mulheres maior de 20 anos.')
# Precisei aprender uma forma nova de usar o modulo random para automatizar o exercicio. 13/03/23

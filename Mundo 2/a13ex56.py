idgeral = []
mvelho = 0
namevelho = ''
mulheres = 0

for c in range(1,4+1):
    print('-=-=- {}ª PESSOA -=-=-'.format(c))
    name = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    # A linha a seguir calcula media ( é muito eficiente ).
    idgeral += [idade]
    soma = sum(idgeral)
    media = soma / len(idgeral)

    # A linha a seguir verifica qual o homem é mais velho.
    if ( c == 1 and sexo in 'Mm'):
        mvelho = idade
        namevelho = name
    if ( idade > mvelho and sexo in 'Mm'):
        mvelho = idade
        namevelho = name

    # A linha a seguir verifica quantas mulheres são maior de 20 anos.
    if ( idade >= 20 and sexo in 'Ff'):
        mulheres += 1

print('A média de idade é {}.\nO Homem mais velho se chama {}.\nE ao todo são {} mulheres maior de 20 anos.'.format(media,namevelho,mulheres))
# Passei sufoco nessa lição, e precisei de ajuda em praticamente tudo. 07/03/23
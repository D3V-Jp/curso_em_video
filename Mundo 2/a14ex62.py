print('\033[4;35mVejamos a progressão aritmética\033[m')
ini = int(input('Escolha o inicio: '))
razão = int(input('Escolha a razão: '))
resu = 0
resu2 = 0
todos = 0
continuar = ''

while continuar != 'N':
    while resu < 10:
        print(ini, end=', ')
        ini += razão
        resu += 1

    while continuar != 'N':
        continuar = str(input('Você quer continuar [S/N]? ').upper())

        if continuar == 'S':

            ad = int(input('Quanto mais vezes? '))
            todos += ad

            if ad > 0:
                while resu2 < todos:
                    print(ini, end=', ')
                    ini += razão
                    resu2 += 1
            if ad == 0:
                continuar = 'N'
# Peguei resposta do video pois não consegui acompanhar o raciocinio. 10/03/23
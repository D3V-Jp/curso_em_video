from random import randint

bot = randint(1,3)
print(bot)
op = int(input('''
SELECIONE UMA DAS OPÇÕES PARA JOGAR JOKENPÔ:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA\n: '''))

if bot == op:
    print('HOUVE EMPATE!')
elif ( bot == 1 and op == 2 ) or ( bot == 2 and op == 3 ) or ( bot == 3 and op == 1):
    print('VOCÊ VENCEU!')
elif op >= 3:
    print('POR FAVOR! SELECIONE UMA OPÇÃO VALIDA.')
else: print('VOCÊ PERDEU! LOSER..')

# EU PEGUEI A LOGICA DE OUTRO CARA NOS COMENTARIO, LOGICA ESSA QUE É INCRIVEL DEMAIS!
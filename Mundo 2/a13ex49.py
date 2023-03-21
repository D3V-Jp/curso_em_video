from time import sleep

tabuada = int(input('Qual tabuada você deseja visualizar?:   '))
print('=-'*20)
for c in range(1,11):
    sleep(0.5)
    print('{} x {} = {}'.format(tabuada,c,tabuada*c))
print('=-'*20)
# Esse exigiu um raciocinio logico. mid-diff 01/03/23
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Pedro' : randint(1,6),
        'Pablo' : randint(1,6),
        'julio' : randint(1,6),
        'Cesar' : randint(1,6)} 
ranking = list()

print('valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou o {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}' )
    sleep(1)



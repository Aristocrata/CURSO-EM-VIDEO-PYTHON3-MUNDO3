"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
maior = '', 0
ordem = [{}, {}, {}, {}]
players = {'jogador 1': 0, 'jogador 2': 0, 'jogador 3': 0, 'jogador 4': 0}
for c in range(1, 5):
    players[f'jogador {c}'] = randint(1, 6)
print(players)
for c in range(0, 4):
    for l, i in players.items():
        if l == 'jogador 1':
            maior = 'jogador 1', i
        elif i > maior[1]:
            maior = l, i
    ordem[c] = maior
    players.__delitem__(maior[0])
    maior = '', 0
print(maior)
print(ordem)

lugar = 0
for l in ordem:
    lugar += 1
    print(f'o número do {l[0]} é {l[1]}, e ele esta em {lugar}° lugar')
"""Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

def ficha(nome='', gol=''):
    if nome == '':
        nome = 'DESCONHECIDO'
    if not gol.isdigit():
        gol = 0
    print(f'O jogador {nome} fez {gol} gols no campeonato')


nome = input('Nome do Jogador: ').strip().title()
gol = input('Nº de gols: ').strip()
ficha(nome, gol)
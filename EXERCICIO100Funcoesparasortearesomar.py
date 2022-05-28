"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint
from time import sleep


def sort(valor):
    lista = []
    for c in range(0, valor):
        lista.append(randint(0, 10))
    print(f'Sorteando {valor} valores da lista: ', end='')
    for c in lista:
        print(f'{c}', end=' ')
        sleep(0.3)
    print('PRONTO!')
    def pares(par):
        soma = 0
        for c in par:
            if c % 2 == 0:
                soma += c
        print(f'Somando os valores pares de {lista}, temos {soma}')
    pares(lista)


sort(5)
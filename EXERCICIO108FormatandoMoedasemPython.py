"""Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado."""

SCRIPT:
from pacote.modulo import *


preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}')
print(f'Aumentando 10% nós temos {moeda(aumentar(preco))}')


MÓDULO:
def aumentar(valor):
    return valor + (valor / 100 * 10)


def dobro(valor):

    return valor * 2


def metade(valor):

    return valor / 2


def moeda(valor):

    return f'R${valor:.2f}'.replace('.', ',')
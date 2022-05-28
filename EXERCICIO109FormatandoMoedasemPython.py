"""Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

def aumentar(v, formatado=False):
    valor_aum = v + (v * 0.1)
    if formatado == False:
        return valor_aum
    else:
        return moeda(valor_aum)

def diminuir(v, formatado=False):
    valor_dim = v - (v * 0.1)
    if formatado == False:
        return valor_dim
    else:
        return moeda(valor_dim)
def dobro(v, formatado=False):
    dobro = v * 2
    if formatado == False:
        return dobro
    else:
        return moeda(dobro)
def metade(v, formatado =False):
    met = v / 2
    if formatado == False:
        return met
    else:
        return moeda(met)

def moeda(valor, moeda='R$'):
    val = f'{moeda} {valor:.2f}'
    val = val.replace('.', ',')
    return val

# @Fábio C Nunes - 30.06.20
from exer108 import moeda
while True:
    valor = str(input('Digite o preço: R$ '))
    print('-' * 50)
    if valor.isnumeric():
        valor = float(valor)
        print(f'A metade de {moeda.moeda(valor)} é: \n{moeda.metade(valor, True)}')
        print('-' * 50)
        print(f'O dobro de {moeda.moeda(valor)} é: \n{moeda.dobro(valor, True)}')
        print('-' * 50)
        print(f'O valor {moeda.moeda(valor)} acrecido de 10% é de:  \n{moeda.aumentar(valor, True)}')
        print('-' * 50)
        print(f'O valor {moeda.moeda(valor)} decrecido de 10% é de: \n{moeda.diminuir(valor, True)}')
        print('-' * 50)
        break
    else:
        print('Digite um valor numérico! ')
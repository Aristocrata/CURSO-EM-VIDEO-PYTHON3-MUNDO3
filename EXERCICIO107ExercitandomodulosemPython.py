"""Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções."""
 
#Módulo moeda:
def aumentar(num):
    mais = num
    mais += num * (10 / 100)
    return mais


def diminuir(num):
    menos = num
    menos -= num * (15 / 100)
    return menos


def dobro(num):
    dobroNum = num * 2
    return dobroNum


def metade(num):
    meio = num / 2
    return meio




#Programa que importou o módulo moeda:
import moeda


user = float(input('Digite um preço: R$'))
print(f'Aumento de 10%, temos {moeda.aumentar(user)}')
print(f'Tirando 15%, temos {moeda.diminuir(user)}')
print(f'O dobro de {user} é tanto {moeda.dobro(user)}')
print(f'A metade de {user} é {moeda.metade(user)}')
"""Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""

def Escreva(palavra):
    tamanho = len(palavra)+4
    print("-"*(tamanho))
    print(f'  {palavra.center(tamanho)}')
    print("-"*(tamanho))

palavra = input("Digite qualquer palavra: ")
print(Escreva(palavra=palavra))
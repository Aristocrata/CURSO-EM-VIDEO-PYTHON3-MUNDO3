"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:"""

from time import sleep

def contador(i, f, p):
    print('~' * 30)
    print(f'\033[4mCONTAGEM DE {i} A {f} DE {p} EM {p}\033[m:')
    if p == 0:
        p = 1
    if i > f:
        for c in range(i, f - p, -p):
            if c < f:
                break
            print(c, end=' ')
            sleep(0.3)
    else:
        for c in range(i, f + p, p):
            if c > f:
                break
            print(c, end=' ')
            sleep(0.3)
    print('FIM!')

# Programa principal
contador(10, 0, 2)
contador(0, 10, 1)
print('-' * 30)
print('Agora é sua vez. Personalize sua contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
pulo = int(input('Pulo: '))
contador(início, fim, pulo)
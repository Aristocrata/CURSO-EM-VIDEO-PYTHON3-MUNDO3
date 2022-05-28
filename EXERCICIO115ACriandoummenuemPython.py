"""Exercício Python 115a: Vamos criar um menu em Python, usando modularização."""

def abertura():
    print('=-'*18)
    print('Cadastramento de pessoas')
    print('=-')
def linha():
    print('=-'*18)
while True:
    abertura()
    print('\033[1;36mDigite 1 para cadastrar uma nova pessoa\033[m')
    print('\033[1;36mDigite 2 para mostrar pessoas cadastradas\033[m')
    print('\033[1;36mDigite 3 para sair do programa\033[m')
    op=int(input('Sua opção:'))
    if op == 1:
        linha()
        print('Opção 1')
    elif op == 2:
        linha()
        print('Opção 2')
    elif op == 3:
        break
    else:
        print('\033[1;31mOpção inválida\033[m')
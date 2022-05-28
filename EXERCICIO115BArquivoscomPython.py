"""Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python."""

#Programa principal 

from pasta import *

menu()

#No pacote pasta:

def linha(msg):
    print('-' * 50)
    print(f'{msg}')
    print('-' * 50)

def inteiro(num):
    while True:
        try:
            valor = int(input(num))
        except (TypeError, ValueError):
            print('\033[31m Erro, tente de novo. \033[m')
        except (KeyboardInterrupt):
            print('\033[31m Usuário não quis digitar. \033[m')
            return 0
        else:
            return valor

def existeA(arq):
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
            
def criaA(arq):
    try:
        arquivo = open(arq, 'wt+')
        arquivo.close()
    except:
        print('Erro na Criação do Arquivo.')
    else:
        print(f'Arquivo: {arq} Criado com Sucesso !')
            
def lerA(arq):
    try:
        arquivo = open(arq, 'rt')
    except:
        print('Erro de Leitura do Arquivo.')
    else:
        print(arquivo.read())
 
def menu():
    from time import sleep
    arq = 'pessoas.txt'
    
    if not existeA(arq):
        criaA(arq)
    
    while True:
        linha(f'{"Menu Principal":>32}')
        print('\033[33m1 - \033[32mVer pessoas cadastradas')
        print('\033[33m2 - \033[32mCadastrar nova Pessoa')
        print('\033[33m3 - \033[32mSair do Sistema \033[m')
        print('-' * 50)

        opcao = inteiro('\033[36mDigite a sua opção: \033[m')
        if opcao <= 0 or opcao > 3:
            print('Erro')
        elif opcao == 1:
            linha(f'{"Ver pessoas cadastradas":>37}')
            lerA(arq)
        elif opcao == 2:
            linha(f'{"Opção 2":>28}') 
        else:
            print('\nSaindo do Programa...')
            sleep(1)
            print('\nVolte Sempre !')
            exit()
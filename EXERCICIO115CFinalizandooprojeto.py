"""Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python."""

from time import sleep
Pessoas = open('ex114.txt', 'a+')
print('~'*10,'PROGRAMA INCRÍVEL 0o0','~'*10)
decisão = 0
while decisão != '2':
    if decisão == '0':
        nome = input('nome:')
        idade = input('idade:')
        print('')
        Pessoas.write(nome)
        Pessoas.write('-')
        Pessoas.write(idade)
        Pessoas.write('\n')
    if decisão == '1':
        Pessoas.seek(0,0)
        print(Pessoas.read())
    decisão = input('\ncadastrar alguém na lista [0]\nVer a lista até agora [1]\nFechar programa [2]\n')
    if decisão != '0' and decisão != '1' and decisão != '2':
        print('dados inválidos, aguarde o programa reiniciar',end='')
        sleep(0.7)
        print('.',end=''),sleep(0.4), print('.',end=''), sleep(0.4), print('.')
Pessoas.close()
sleep(0.1)
print('Desligando',end='')
print('.',end=''),sleep(0.4), print('.',end=''), sleep(0.4), print('.',end=''),sleep(0.4),print('.')
print('OBRIGADO POR USAR')


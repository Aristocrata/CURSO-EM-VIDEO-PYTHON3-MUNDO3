"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico"""

def LeiaInt(num):
    while True:
        n = input(num)
        if n.isnumeric() is False:
            print('\033[1;3;31mERROR! Digite um numero inteiro válido.\033[m')
        else:
            return n

number = LeiaInt(f'{"=-"*20}=\ndigite um numero: ')
print(f'Você cabou de digitar o numero {number} válido.')
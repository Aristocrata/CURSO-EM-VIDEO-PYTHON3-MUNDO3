"""Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

def voto(nascimento):

    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, seu Voto é Opcional.'
    elif idade >= 18:
        return f'Com {idade} anos, o Voto é Obrigatório'
    else:
        return f'Com {idade} anos, Não pode Votar.'

nascimento = int(input('Digite o ano de seu nascimento: '))
print(voto(nascimento))
"""Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""

def metade(pre, sit):
    r = pre / 2
    if sit == True:
        return moeda(r)
    if sit == False:
        return r


def dobro(pre, sit):
    r = pre * 2
    if sit == True:
        return moeda(r)
    if sit == False:
        return r


def aumentar(pre, taxa, sit):
    r = pre + (pre * taxa/100)
    if sit == True:
        return moeda(r)
    if sit == False:
        return r


def diminuir(pre, taxa, sit):
    r = pre - (pre * taxa/100)
    if sit == True:
        return moeda(r)
    if sit == False:
        return r


def moeda(pre):
    return f'R${pre:.0f},00'


def resumo(pre, t1, t2):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:   {moeda(pre)}')
    print(f'Dobro do preço:    {dobro(pre, True)}')
    print(f'Metade do preço:   {metade(pre, True)}')
    print(f'{t1}% de aumento:    {aumentar(pre, t1, True)}')
    print(f'{t2}% de redução:    {diminuir(pre, t2, True)} ')
    print('-'*30)
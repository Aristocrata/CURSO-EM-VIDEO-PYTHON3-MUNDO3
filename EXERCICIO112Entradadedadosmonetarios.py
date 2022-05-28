"""Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários."""

def leiadinheiro(p):
    while True:
        cont = 0
        p = input(str('Digite o preço: R$'))
        for letra in p:
            if letra == '.' or letra == ',':
                cont += 1
        if cont > 1:
            print(f'ERRO: "{p}" é um dado inválido.')
        elif (p.replace('.', '')).isnumeric() or (p.replace(',', '')).isnumeric():
            p = p.replace(',', '.')
            break
        else:
            print(f'ERRO: "{p}" é um dado inválido.')
    return float(p)
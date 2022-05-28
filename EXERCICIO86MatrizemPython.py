linhas = int(input('Quantas linhas? '))
colunas = int(input('Quantas colunas? '))
matriz = [[], [], []]
for i in range(0, linhas):
    for j in range(0, colunas):
        n = int(input(f'Digite o valor ({i},{j}): '))
        matriz[i].append(n)
for i in range(0, linhas):
    for j in range(0, colunas):
        print(f'[ {matriz[i][j]:^3} ]', end='')
    print()
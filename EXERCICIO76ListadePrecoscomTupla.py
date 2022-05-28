print(54*'-')
print(15*' ', 'LISTAGEM DE PREÇOS')
print(54*'-')
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caneta', 1.20, 'Caderno', 7.50, 'Lapiseira', 1.99)
for i in range(0, 10, 2):
    j = i + 1
    pontinhos = (44-len(lista[i]))*'.'
    print(f'{lista[i]} {pontinhos} R$ {lista[j]:>.2f}')
print(54*'-')
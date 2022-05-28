lista = []
lista.sort()
sn = 'S'
while sn == 'S':
    add = int(input('Digite um valor qualquer: '))
    if add not in lista:
        lista.append(add)
    else:
        print('Número repetido.')
    sn = str(input('Deseja continuar: ')).strip().upper()
print(lista)
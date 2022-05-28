grupo = list()
pesa = leve = 0
while True:
    pessoa = list()  # Refaz a lista a cada volta
    pessoa.append(str(input('Nome: ')).title())
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa.copy())
    pesa = pessoa[1] if len(grupo) == 1 or pessoa[1] > pesa else pesa
    leve = pessoa[1] if len(grupo) == 1 or pessoa[1] < leve else leve
    ask = str(input('\tQuer continuar? [S/N]: ')).lower().strip()
    if ask[0] == 'n':
        break
print('-' * 30, f'\nAo todo foram cadastradas {len(grupo)} pessoas.')
print(f'O mais pesado foi {pesa:.1f}kg, foram: ', end='')
for p in grupo:
    print(f'[{p[0]}] ' if p[1] == pesa else '', end='')
print(f'\nO mais leve foi {leve:.1f}kg, foram: ', end='')
for p in grupo:
    print(f'[{p[0]}] ' if p[1] == leve else '', end='')
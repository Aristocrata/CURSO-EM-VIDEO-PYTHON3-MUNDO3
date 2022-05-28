a = [float(input('Insira um número: ')) for i in range(0, 5)]
print(f'Foram digitados {len(a)} números!')
a.sort(reverse=True)
print(f'Em ordem decrescente {a}')
print(f'O valor 5{" " if  5 in a else " não"}está na lista')
ex = str(input('Digite uma expressão: '))
pa = []
pf = []
for sim in ex:
    if sim == '(':
        pa.append(sim)
    elif sim == ')':
        pf.append(sim)
print(pa)
print(pf)
if len(pa) == len(pf):
    print('Sua expressão esta correta.')
else:
    print('Sua expressão esta incorreta.')
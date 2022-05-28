from random import sample
from time import sleep
print('-'*30+'\n'+'     JOGA NA MEGA SENA       \n'+'-'*30)
matriz=[]
o=int(input('Quantos jogos quer que eu sorteie? '))
for i in range(0,o):
    matriz.append([])
print('-='*3+f' SORTEANDO {o} JOGOS '+'-='*3)
for i in range(0,o):
    matriz[i]=sample(range(60),6)
    sleep(1)
    print(f'Jogo {i+1}: {matriz[i]}')
"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

jogador, gol = {}, []
jogador['nome'] = str(input("Nome:"))
partidas = int(input(f"quantas partidas {jogador['nome']} jogou? "))
for p in range(0, partidas):
    gol.append(int(input(f"Qunatos gols na  partida {p}? ")))
jogador['gols'] = gol
soma = sum(gol)
jogador['total'] = soma
print("-=-"*20)
print(jogador)
print("-=-"*20)
for key, value in jogador.items():
    print(f"O {key} tem valor {value}")
print("-=-"*20)
for v, it in enumerate(gol):
    print(f"Na partida {v+1} o(a) {jogador['nome']} fez {it} gols")
print(f"O jogador(a) fez o total de {soma} gols")
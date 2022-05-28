from random import sample

numeros = tuple((sample(range(0, 11), 5)))

print(f"Os números gerados foram: {numeros}")
print(f"O array é do tipo {type(numeros)}")
print(f"O maior número é {max(numeros)} e o menor é {min(numeros)}.")
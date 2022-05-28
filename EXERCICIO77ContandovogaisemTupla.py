palavras = ('lista', 'palavra', 'jagunço', 'jaguara', 'cavalheiro', 'joao', 'camaro', 'cavalo', 'jabiru', 'cacique')

for c in range(0, len(palavras)):
    print(f'\nNa {(c+1)}° palavra estão as vogais: ', end='')
    for d in range(0, len(palavras[c])):
        if palavras[c][d].lower() in 'aeiou':
            print(f'{palavras[c][d]} ', end='')
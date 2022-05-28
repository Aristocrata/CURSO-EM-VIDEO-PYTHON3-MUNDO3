from time import sleep
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino','Athletico-PR', 'Internacional', 'Fluminense',
         'Atlético-GO', 'Cuiabá', 'Ceará', 'São Paulo', 'América-MG', 'Juventude', 'Santos', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
print('Informações sobre os times do Brasileirão')
pergunta = ' '
while pergunta != 'N':
    while True:
        sleep(2)
        escolha = int(input('Entre as opções\n'
                            '[ 1 ] para os 5 primeiros classificados\n'
                            '[ 2 ] para os 4 últimos classificados\n'
                            '[ 3 ] para todos os classificados em ordem alfabética\n'
                            '[ 4 ] para a classificação de algum dos times\n'
                            '[ 5 ] para encerrar.\nEscolha:'))
        if escolha == 1:
            print(f'Os 5 primeiro classificados no Brasileirão são:')
            for t in times[:5]:
                print(f'{times.index(t)+1}º', t)
        elif escolha == 2:
            print(f'Os 4 últimos classificados no Brasileirão são:')
            for f in times[-4:]:
                print(f'{times.index(f)+1}º', f)
        elif escolha == 3:
            print(f'Os 20 classificados do Brasileirão em ordem alfabética são:')
            for t in sorted(times):
                print(t)
        elif escolha == 4:
            nome = str(input('De qual time você quer saber? ')).strip().capitalize()
            if nome in times:
                print(f'O time {nome} está em {times.index(nome) + 1}º na tabela.')
            else:
                print(f'O {nome} não está classificado para o brasileirão.')
        elif escolha == 5:
            break
        sleep(2)
    pergunta = str(input('Quer escolher entre as opções novamente? ')).strip().upper()[0]
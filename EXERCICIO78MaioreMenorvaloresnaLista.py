nums = []
numsbackup = []
maiormenor = ['menor', 'maior']
print('='+'-='*30)
for a in range(0, 5):
    nums.append(int(input(f'Digite um valor para a posição {a}: ')))
    if a == 4:
        print('='+'-='*30)
        numsbackup += nums
        print(f'Você digitou os valores: {nums}', end='')
        nums.sort()
        for b in range(-1,1):
            print(f'\nO {maiormenor[b]} valor digitado foi {nums[b]} nas posições ', end='')
            for c in range(0, len(numsbackup)):
                if numsbackup[c] == nums[b]:
                    print(c, end='... ')
print('\n')
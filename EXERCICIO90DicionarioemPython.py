"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""

dic = dict()
dic["nome"] = str(input("Nome do aluno : "))
dic["média"] = float(input(f'Media de {dic["nome"]} : '))
print(f'O aluno {dic["nome"]} tem média igual a {dic["média"]} ')
if dic["média"] >= 7 :
    print(f'O aluno {dic["nome"]} foi APROVADO !!!')
else :
    print(f'O aluno {dic["nome"]} foi REPROVADO !!!')
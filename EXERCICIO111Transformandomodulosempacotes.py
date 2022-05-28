"""Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""

# PROGRAMA PRINCIPAL:

from CeV.utilidadescev.moeda import resumo
                                       # Usam-se pontos para representar as barras no path.
                                       # Tive que especificar o DIRETÓRIO em que o pacote está! Sem isso, o programa não o reconhecia.
                            
q = float(input('Digite um valor:  R$'))
t = float(input('Digite a taxa (%): '))

resumo(q, t, True)
"""
Operadores Relacionais
== > >= < <= !=
"""

nome = input('qual é o seu nome? ')
idade = int(input('qual a sua idade? '))

idade_min = 20
idade_max = 30

if idade >= idade_min and idade <= idade_max:
    print(f'{nome} pode pegar o empréstimo.')

else:
    print(f'{nome} NÂO pode pegar o empréstimo.')
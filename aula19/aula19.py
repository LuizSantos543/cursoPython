"""
while em Python
utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos entender condições e operadores.
"""

'''while True: # loop infinito
    nome = input("Qual é o seu nome? ")
    print(f'Olá {nome}!')
'''
'''
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print (x)
    x = x + 1

print('Acabou!')
'''

x = 0 # linha

while x < 10:
    y = 0  # coluna

    while y < 5:
        print(f'X vale {x} e Y vale {y}.')
        y += 1

    x += 1 # x = x + 1

print('Acabou')
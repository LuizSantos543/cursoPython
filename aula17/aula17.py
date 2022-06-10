"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
frase = 'Algoritmos e ProgramaçãO de Computadores I'
contLetra = 0
for c in frase:
    if c in 'oO':
        print('Vogal: ', c)
        contLetra += 1
print('Total de letras o ou O: ', contLetra)

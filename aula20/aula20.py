"""
While / Else
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')# só executa quando o valor do while for false
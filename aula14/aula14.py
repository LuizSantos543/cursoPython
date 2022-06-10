num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# isnumeric
# isdigit
# isdecimal

# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#
#     print(num1 + num2)
# else:
#     print('Não foi possível converter os números para realizar contas.')
#
# # as funções isdigit, isnumeric e isdecimal só opera com números positivos inteiros.

try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except:
    print('ERROR')
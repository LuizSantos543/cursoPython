while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    if not num1.isnumeric() or not num2.isnumeric:
        print('Você precisa digitar um número.')
        continue
    op = input('Digite um operador: ')

    num1 = int(num1)
    num2 = int(num2)

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print('Operador inválido!')

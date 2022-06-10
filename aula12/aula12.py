"""
Operadores Lógicos
and, or, not
in e not in
"""
# nome = 'Luiz'
#
# if 'qaq' in nome:
#     print("Existe")
# else:
#     print('não existe')

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Login efetuado com sucesso!')

else:
    print('Usuário ou senha inválidos')
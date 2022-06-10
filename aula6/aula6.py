"""
Iniciar com letra, pode conter numeros, separa _, letras minúsculas
"""
nome ='Luiz'
idade = 24
altura = 1.70
e_maior = idade > 18
peso = 60
imc = peso / altura ** 2

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior: ', e_maior)


print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
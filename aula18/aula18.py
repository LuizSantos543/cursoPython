"""
Manipulando Strings -  Aula 6
* String indices
* Fatiamneto de Strings [inicio:fim:passo] (o fim não é incluido. Deve -se colocarum número depois do carecter desejado)
* Funções buly-in len, abs, type, print, etc...
Essas funcões podem ser usadas diretamente em cada tipo.
"""
# positivos  [012345678]
texto = 'Python s2'
# negativos -[987654321]
url = 'www.google.com.br/'
print(url[:-1])

string1 = texto[-9]
string2 = texto[0:6:2]
print(string1)
print(string2)
print(len(texto))

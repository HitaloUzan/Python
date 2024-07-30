# Estudos em Python.
# Aula  Print
print("Hello World")
print("How are you ?")
print("I am fine and you ?")

# Aula 2 Comentarios
# Use a '#' para fazer um comentario de uma linha

'''Comentarios com mais de uma linha use as três aspas'''

x = 2

print(x)

y = ('olá')

print(y)

# Modificando o tipo de dado

x = str(3)
y = int(4)
z = float(5)


print(x + x)
print(y + y)
print(z + z)

# Pratica 

#  O Hitalo tem 26 anos de idade e mora na cidade de São Paulo



nome = input('Qual é o seu nome ? ')
idade = input('Qual é a sua idade ? ')
cidade = input('Qual é a sua cidade ? ')

print('O '+ nome + ' tem ' + str(idade) + ' anos de idade e mora em ' + cidade + '.')


ano = int(input('Em que ano você nasceu ? '))

idade = 2024 - ano

print('Você nasceu em ' + str(ano) + ' por tanto tem ' + str(idade) + ' de idade' + '.')

print(type(idade))
print(type(ano))

fruta = 'Abacate'

print(fruta[-1])

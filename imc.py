nome = 'Eduardo Martins'
altura = 1.78
peso = 50
imc = peso / altura ** 2

# Eduardo tem 1.78 de altura
# pesa 50 quilos e seu imc é
# 15.780835753061481

print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e sei imc é')
print(imc)

print(' ')

linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'
print(linha1)
print(linha2)
print(linha3)

from random import randint
num = str(randint(100000000, 999999999))

lista = ''
cpf = ''
soma1 = 0
soma2 = 0

# Gerando digito 1 
for p, r in enumerate(range(10,1,-1)):
        x = int(num[p])*int(r)
        soma1 += x
        lista += num[p]

# print(soma1)
valor = 11 - (soma1 % 11)

if valor > 9:
    valor = '0'
else:
    valor = str(valor)

# print(f'Digito1 é {valor}')
lista += valor

# Gerando digito 2
for a, b in enumerate(range(11,1,-1)):
    c = int(lista[a])*int(b)
    soma2 += c

# print(soma2)
valor2 = 11 - (soma2 % 11)

# print(f'Digito2 é {valor2}')
lista += (str(valor2))

# Formatando o CPF
for i, v in enumerate(range(0,11,1)):
    if v == 3 or v == 6:
        cpf += '.'
    if v == 9:
        cpf += '-'

    cpf += lista[i]

print(f"CPF gerado: {cpf}")

cpf = input('Digite seu CPF: ')
lista = ''
soma1 = 0
soma2 = 0

cpfn = ''.join(filter(str.isnumeric, cpf))

# Cálculo do digito 1
for i, v in enumerate(range(10,1,-1)):
        x = int(cpfn[i])*int(v)
        soma1 += x
        if i < 9:
            lista += cpfn[i]
        # print(f'{cpfn[i]} * {v} = {x}')

# print(soma1)
valor = 11 - (soma1 % 11)

if valor > 9:
    valor = '0'
else:
    valor = str(valor)

# print(f'Digito1 é {valor}')
lista += valor

# Cálculo do digito 2
for a, b in enumerate(range(11,1,-1)):
    c = int(lista[a])*int(b)
    soma2 += c
    # print(f'{lista[a]} * {b} = {c}')

# print(soma2)
valor2 = 11 - (soma2 % 11)

# print(f'Digito2 é {valor2}')
lista += str(valor2)

# Eliminando as sequências
sequencia = ''.join(cpfn) == (str(lista[0])) * len(cpfn)    

# Validando o CPF
if lista == cpfn and not sequencia:
    print(f'{cpf} - CPF VÁLIDO')
else:
    print(f'{cpf} - CPF INVÁLIDO')

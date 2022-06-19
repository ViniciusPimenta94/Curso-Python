print('CÁLCULO DE IMC\n')

n = input('Digite seu nome: ')
i = input('Qual a sua idade? ')
h = input('Qual a sua altura? ')
p = input('Qual é o seu peso? ')
imc = float(p)/(float(h)**2)

print(f'\n{n} tem {i} anos, {h} de altura e pesa {p} kg.')
print(f'O IMC de {n} é {imc:.2f}.')

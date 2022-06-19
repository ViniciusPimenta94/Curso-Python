"""
- Digite um número, falar se é par ou ímpar, informar caso não seja número inteiro.
- Digite a hora e diga bom dia, tarde ou noite.
- Digite o nome e se tiver 4 letras ou menos, dizer que o nome é curto. De 5 a 6, normal e mais que 6, grande.
"""
#Ex1
n = input('Digite um número: ')

try:
    n = int(n)
    if (n%2 == 0):
        print(f'{n} é PAR')
    else:
        print(f'{n} é ÍMPAR')
except:
    print('Você não digitou um número inteiro')

print('*****************************************************')

#Ex2
h = input('Que horas são? ')

try:
    h = int(h)
    if (h>=0) and (h<=11):
        print('BOM DIA')
    elif (h>=12) and (h<=17):
        print('BOA TARDE')
    elif (h >= 18) and (h <= 23):
        print('BOA NOITE')
    else:
        print('Você não digitou um horário válido')
except:
    print('Você não digitou a hora corretamente')

print('*****************************************************')

#Ex3
nome = input('Digite seu nome: ')

if not nome.isdigit():
    qdt = len(nome)
    if (qdt<=4):
        print('Seu nome é curto')
    elif (qdt>=5) and (qdt<=6):
        print('Seu nome é normal')
    elif (qdt > 6):
        print('Seu nome é grande')
else:
    print('Você não digitou seu nome corretamente')

import re

regressivo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

# Função principal 
def validar(cnpj):
    cnpj = remover_caracteres(cnpj)
    
    try:    
        if sequencia(cnpj):
            print('Inválido, pois é uma sequência')
            return False
    except:
        return False
    
    try:    
        novo_cnpj = calcular(cnpj=cnpj, digito=1)
        novo_cnpj = calcular(cnpj=novo_cnpj, digito=2)
    
    except Exception as e:
        return False
    
    if novo_cnpj == cnpj:
        return True
    else:
        return False

# Formatando o CNPJ para o cálculo
def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

# Verificando se é uma sequência
def sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    
    if sequencia == cnpj:
        return True
    else:
        return False

# Cálculo dos 2 digitos finais do CNPJ
def calcular(cnpj, digito):
    if digito == 1:
        regr = regressivo[1:]
        novo_cnpj = cnpj[:-2]
        
    elif digito == 2:
        regr = regressivo
        novo_cnpj = cnpj
        
    else:
        return None
    
    total = 0
    
    for i, v in enumerate(regr):
        total += int(cnpj[i])*v
        
    digito = 11 - (total % 11)
    
    digito = digito if digito <= 9 else 0
    
    return f'{novo_cnpj}{digito}'

# Valores para teste
cnpj = '042.252.011/0001-10'
cnpj2 = '23664303000104'
cnpj3 = '17178195004588'

# Validando o CNPJ
if validar(cnpj):
    print(f'{cnpj} é válido')
else:
    print(f'{cnpj} é inválido')

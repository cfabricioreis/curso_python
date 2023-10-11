""" 
Cálculo do Primeiro Dígito Verificador do CPF:

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2  
 * 7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
--> 70+36+48+56+12+20+32+27+0= 301
Multiplicar o resultado anterior por 10
--> 301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
--> 3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7


Cálculo do Segundo Dígito do CPF:
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DÍGITO, 
multiplicando cada um dos valores por uma 
contagem regressiva começando de 11

"""

# considerando que usuário digitará apenas os dígitos do cpf, sem pontuação
cpf_digitado = input('Informe o número de CPF:')
nove_digitos = cpf_digitado[:9]

# passo 1 - cálculo dos elementos do cpf
contador_regressivo_digito_1=10
soma_elementos=0
for digito in nove_digitos:
    soma_elementos += (int(digito) * contador_regressivo_digito_1)
    contador_regressivo_digito_1-= 1

# passo 2 - multiplica a soma dos elementos por 10
soma_elementos *= 10

# passo 3 - Cálculo do resto da divisão por 11
digito_1= soma_elementos % 11
digito_1 = digito_1 if digito_1 <=9 else 0

# print (f'O primeiro dígito do CPF informado {cpf_digitado} foi calculado, e o resultado é igual a {digito_1}.')
contador_regressivo_digito_2=11
soma_elementos= 0
for digito in nove_digitos:
    soma_elementos += (int(digito) * contador_regressivo_digito_2)
    contador_regressivo_digito_2-= 1

soma_elementos += (digito_1 * contador_regressivo_digito_2)

soma_elementos *= 10

digito_2= soma_elementos % 11
digito_2= digito_2 if digito_2 <= 9 else 0

print(f'Os digitos verificadores calculados foram {digito_1} e {digito_2}')


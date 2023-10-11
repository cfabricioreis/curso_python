import random
import sys
'''
1    Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins;
2    Pará, Amazonas, Acre, Amapá, Rondônia e Roraima;
3    Ceará, Maranhão e Piauí;
4    Pernambuco, Rio Grande do Norte, Paraíba e Alagoas;
5    Bahia; e Sergipe;
6    Minas Gerais;
7    Rio de Janeiro e Espírito Santo;
8    São Paulo;
9    Paraná e Santa Catarina;

0   Rio Grande do Sul.
'''

emissor_cpf= ['RS',                          
              'DF, GO, MS ou TO', 
              'PA, AM, AC, AP, RO, RR', 
              'CE, MA, PI', 
              'PE, RN, PB, AL', 
              'BA, SE', 
              'MG', 
              'RJ, ES', 
              'SP',
              'PR, SC']

digitos_cpf= ''
for digito in range(9):
    digitos_cpf+= str(random.randint(0,9))

# print(nove_digitos_cpf)

#calculo do 1o digito verificador do CPF
contador_regressivo=10
soma_digitos= 0
for cont in digitos_cpf:
    soma_digitos+= (int(cont) * contador_regressivo)
    contador_regressivo-= 1

soma_digitos*= 10

digito_1= soma_digitos % 11
digito_1= digito_1 if digito_1 <= 9 else 0

digitos_cpf+= str(digito_1)

# print (f'{digitos_cpf[:9]}-{digitos_cpf[9]}')

#calculo do 2o dígito verificador do CPF
contador_regressivo=11
soma_digitos= 0
for cont in digitos_cpf:
    soma_digitos+= (int(cont) * contador_regressivo)
    contador_regressivo-= 1

soma_digitos*= 10

digito_2= soma_digitos % 11
digito_2= digito_2 if digito_2 <= 9 else 0

digitos_cpf+= str(digito_2)

print (f'CPF gerado: {digitos_cpf[:9]}-{digitos_cpf[9:]}')
print (f'O CPF gerado foi emitido por: {emissor_cpf[int(digitos_cpf[8])]}')
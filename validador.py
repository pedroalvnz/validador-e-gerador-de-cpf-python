import sys

cpf = input('Digite um cpf para ser válidado : ')

cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '') # Organização do CPF
cpf_válido = cpf == cpf[1] * len(cpf)

if cpf_válido:       # Verificação de sequencia do CPF
    print('O CPF está sequenciado')
    sys.exit()
cpf_9 = list(cpf[0:9])

soma_do_num1 = 0
contagem_1 = 10

for i, numero in enumerate(cpf_9):   # Cálculo do num_1
    numero = int(numero)
    soma_do_num1 += numero * (contagem_1 - i)
resultado_operacao_num1 = (soma_do_num1*10) % 11
num_1 = 0 if resultado_operacao_num1 > 9 else resultado_operacao_num1 # Valor do primeiro número depois do '-' 

cpf_9.append(str(num_1))

soma_do_num2 = 0
contagem_2 = 11

for i, numero in enumerate(cpf_9): # Cálculo do num_2
    numero = int(numero)
    soma_do_num2 += numero * (contagem_2 - i)
resultado_operacao_num2 = (soma_do_num2 * 10 )% 11
num_2 = 0 if resultado_operacao_num2 > 9 else resultado_operacao_num2 # Valor do segundo número depois do '-'

cpf_9.append(num_2)
novo_cpf = ''
for numero in cpf_9:      # Fazendo a lista se tornar uma única string
    novo_cpf += str(numero) 

if novo_cpf == cpf:
    print(f'CPF {cpf} válido')
else:
    print('CPF inválido')

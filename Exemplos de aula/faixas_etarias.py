'''
Faça um programa que leia a idade de uma pessoa e informe a sua faixa etária,
sabendo que:
criança     - menor de 12 anos
adolescente - de 12 a 17 anos
adulto      - de 18 a 59 anos
idoso       - a partir de 60 anos
'''

# Solução
idade = int(input("Digite a idade: "))
if idade < 12:
    print("É criança.")
elif idade <= 17:
    print("É adolescente.")
elif idade <= 59:
    print("É adulto.")
else:
    print("É idoso.")

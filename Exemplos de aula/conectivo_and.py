'''
Faça um programa que leia a idade de uma pessoa e informe se ela é ou não é adolescente,
sabendo que adolescentes têm de 12 a 17 anos.
'''

# Solução 1 - sem o uso do conectivo lógico AND
idade = int(input("Digite a idade: "))
if idade >= 12:
    if idade <= 17:
        print("É adolescente.")
    else:
        print("Não é adolescente.")
else:
    print("Não é adolescente.")

# Solução 2 - usando o conectivo lógico AND
idade = int(input("Digite a idade: "))
if idade >= 12 and idade <= 17:
    print("É adolescente.")
else:
    print("Não é adolescente.")
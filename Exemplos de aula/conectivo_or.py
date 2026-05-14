''' 
Faça um programa que leia o nome de uma disciplina da DS102 e informe se ela é técnica ou propedêutica,
sabendo que apenas "LP1" e "ICC" são disciplinas técnicas.
'''

# Solução 1 - sem o uso do conectivo lógico OR
disciplina = input("Digite o nome da disciplina: ")
if disciplina == "LP1":
    print("Disciplina técnica")
elif disciplina == "ICC":
    print("Disciplina técnica")
else:
    print("Disciplina propedêutica")

# Solução 2 - usando o conectivo lógico OR
disciplina = input("Digite o nome da disciplina: ")
if disciplina == "LP1" or disciplina == "ICC":
    print("Disciplina técnica")
else:
    print("Disciplina propedêutica")

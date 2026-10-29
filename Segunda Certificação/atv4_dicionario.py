# Gabarito da atividade que pedia para criar uma lista de alunos, considerando que:
# Cada aluno é um dicionário com nome, turma, nota e estaAprovado.
# A chave estaAprovado deve ser automaticamente verdadeira se a nota for maior ou igual a 6. Caso contrário, deve ser falsa.
# O sistema deve perdir para o usuário cadastrar alunos até digitar sair.
# Após escolher "sair", o sistema deve imprimir todos os alunos cadastrados.

alunos = []

while True:
    nome = input("Digite o nome do aluno (ou sair): ")
    if nome == "sair":
        break
    turma = input("Digite a turma do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 6:
        estaAprovado = True
    else:
        estaAprovado = False
    aluno = {
        "nome": nome,
        "turma": turma,
        "nota": nota,
        "estaAprovado": estaAprovado
    }
    alunos.append(aluno)

for aluno in alunos:
    print("\nREGISTRO DE ALUNO:")
    print(f"Nome: {aluno["nome"]}")
    print(f"Turma: {aluno["turma"]}")
    print(f"Nota: {aluno["nota"]}")
    print(f"EstaAprovado: {aluno["estaAprovado"]}")

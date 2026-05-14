#Leitura da entrada
nome = input("Digite o nome: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

# Processamento
media = (nota1 + nota2) / 2
if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#Escrita da saída
print(f"Boletim de {nome}")
print(f"Média: {media}")
print(f"Situação: {situacao}")

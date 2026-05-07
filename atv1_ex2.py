#Leitura da entrada
nome = input("Digite o nome do funcionário: ")
salario_atual = float(input("Digite o salário atual: "))
vendas = float(input("Digite o valor das vendas do mês: "))

# Processamento
if vendas > 5000:
    bonus = salario_atual * 0.1
else:
    bonus = salario_atual * 0.05

#Escrita da saída
print(f"Nome: {nome}")
print(f"Salário original: {salario_atual}")
print(f"Bônus: {bonus}")
print(f"Salário final: {salario_atual + bonus}")

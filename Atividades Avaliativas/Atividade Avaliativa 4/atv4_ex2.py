contador = 1
soma = 0
numero_final = int(input("Digite o número: "))
while contador <= numero_final:
    soma += contador
    contador += 1
print(f"A soma de todos os números de 1 até {numero_final} é {soma}")
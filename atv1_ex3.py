#Leitura da entrada
numero = int(input("Digite um número: "))

# Processamento
dobro = numero * 2
triplo = numero * 3
if numero % 2 == 0:
    par_ou_impar = "par"
else:
    par_ou_impar = "ímpar"

#Escrita da saída
print(f"Número: {numero}")
print(f"Dobro: {dobro}")
print(f"Triplo: {triplo}")
print(f"O número é {par_ou_impar}")

contador = 0
soma = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if not numero: # é equivalente a numero == 0
        break
    contador += 1
    soma += numero
if not contador:
    media = 0
else:
    media = soma/contador
print(f"Quantidade de números: {contador}")
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")

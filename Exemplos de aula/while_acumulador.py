# Faça um programa para calcular a soma de 10 números digitados pelo usuário.

soma = 0 # a variável soma é um ACUMULADOR porque ela vai acumular o resultado parcial da soma a cada rodada do while
x = 1 # a variável x é um CONTADOR porque ela vai ser usada para contar quantas vezes o while deve ser executado
while x <= 10:
    numero = int(input("Digite um valor: "))
    soma += numero
    print(f"Soma dos {x} primeiros números: {soma}")
    x += 1
print(f"A soma dos 10 números é {soma}")

# Faça um programa para calcular a soma de números digitados pelo usuário até ele digitar 0.
soma = 0
while True:
    numero = int(input("Digite um valor: "))
    if numero == 0:
        break # o break é usado para quebrar o while e seguir para o próximo comando após o while
    soma += numero
    print(f"Soma parcial: {soma}")
print(f"A soma final: {soma}")

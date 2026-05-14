"""
O Comando while serve para repetir um bloco de instruções enquanto uma condição for verdadeira.
"""

# Uso do while para contar de 1 a 3
x = 1
while x <= 3:
    print(x)
    x = x + 1

# Uso do while para contar de 1 a 50
x = 1
while x <= 50:
    print(x)
    x = x + 1

# Uso do while para contar de 50 a 100
x = 50
while x <= 100:
    print(x)
    x = x + 1

#Faça um programa que realize uma contagem regressiva de 10 até 1 e em seguida imprima "Fogo!"
x = 10
while x >= 1:
    print(x)
    x = x - 1
print("Fogo!")

#Faça um programa para contar de 1 até um valor digitado pelo usuário
x = 1
valor_usuario = int(input("Digite um valor: "))
while x <= valor_usuario:
    print(x)
    x = x + 1

    
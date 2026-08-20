# Solução 1
x = 1
valor = int(input("Digite um valor: "))
while x <= 10:
    print(valor * x)
    x += 1

# Solução 2
valor = int(input("Digite um valor: "))
x = valor
while x <= valor * 10:
    print(x)
    x += valor
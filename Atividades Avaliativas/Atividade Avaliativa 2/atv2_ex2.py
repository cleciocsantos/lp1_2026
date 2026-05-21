# Solução 1
x = 0
valor_final = int(input("Digite um valor: "))
while x <= valor_final:
    print(x)
    x += 2

# Solução 2 - exige o dobro de execuções do while em relação à solução 1
x = 0
valor_final = int(input("Digite um valor: "))
while x <= valor_final:
    if x % 2 == 0:
        print(x)
    x += 1
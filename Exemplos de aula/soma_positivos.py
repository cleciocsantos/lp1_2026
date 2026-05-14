# Trabalho desenvolvido por Fulano e Beltrano
print("Olá, este é meu primeiro programa!")
a = 0
b = int(input("Digite o valor de b: "))
if b > 0:
    a = b
else:
    b = -b
    a = a + b
c = int(input("Digite o valor de c: "))
if c < 0:
    c = -c
    a = a + c
else:
    a = a + c
# A próxima linha imprime a resposta na tela
print(f"A soma positiva de b e c é {a}")
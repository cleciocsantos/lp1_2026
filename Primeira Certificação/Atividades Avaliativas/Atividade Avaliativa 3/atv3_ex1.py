x = 0
maior = -1
while x < 10:
     numero = int(input("Digite um número: "))
     if numero > maior:
          maior = numero
     x += 1
print(f"O maior dos 10 número é {maior}")
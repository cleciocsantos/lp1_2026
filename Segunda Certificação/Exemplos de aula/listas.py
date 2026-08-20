# Inicia uma lista vazia.
frutas = []

# Pede ao usuário para digitar 3 frutas e as insere na lista.
contador = 1
while contador <= 3:
    fruta = input(f"Digite a {contador}ª fruta: ")
    frutas.append(fruta)
    contador += 1

# Exibe todas as frutas cadastradas.
print("\nFrutas cadastradas:\n")
for fruta in frutas:
    print(fruta)

# Pede ao usuário para substituir uma fruta na lista.
indice = int(input(f"Digite o indíce onde se quer alterar: "))
fruta = input(f"Digite a fruta substituta: ")
frutas[indice] = fruta

# Exibe novamente as frutas cadastradas após a substituição feita.
print("\nFrutas cadastradas:\n")
for fruta in frutas:
    print(fruta)

# Cria a função de imprimir frutas.
def imprimir_frutas(frutas):
    print("\nFrutas cadastradas:\n")
    for i, fruta in enumerate(frutas):
        print(f"[{i+1}] - {fruta}")

# Inicia uma lista vazia.
frutas = []

# Pede ao usuário para digitar 3 frutas e as insere na lista.
contador = 1
while contador <= 3:
    fruta = input(f"Digite a {contador}ª fruta: ")
    frutas.append(fruta)
    contador += 1

# Chama a função para imprimir todas as frutas cadastradas.
imprimir_frutas(frutas)

# Pede ao usuário para substituir uma fruta na lista.
indice = int(input(f"Digite o indíce onde se quer alterar: "))
fruta = input(f"Digite a fruta substituta: ")
frutas[indice-1] = fruta

# Chama a função para imprimir todas as frutas cadastradas.
imprimir_frutas(frutas)

# Pede ao usuário para excluir uma fruta na lista.
indice = int(input(f"Digite o indíce da frutas que se quer excluir: "))
frutas.pop(indice-1)

# Chama a função para imprimir todas as frutas cadastradas.
imprimir_frutas(frutas)
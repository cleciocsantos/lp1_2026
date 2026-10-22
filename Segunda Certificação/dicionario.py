# Criação de um dicionário com várias chaves e valores.
dinossauro1 = {
    "peso": 7.2,
    "especie": "oxalaia",
    "estaVivo": False
}

# Impressão do valor em uma chave específica.
print(dinossauro1["especie"])

# Atualização do valor em uma chave
dinossauro1["especie"] = "velocirápido"

# Criação de uma nova chave no momento da atribuição de valor
dinossauro1["idade"] = 12

chave = "idade"

# Testando se uma chave existe em um dicionário
if chave in dinossauro1:
    print(dinossauro1[chave])
else:
    print(f"Não tem {chave} cadastrada")

# Criação de um dicionário vazio
dinossauro2 = {}

# Atribuindo um valor digitado pelo usuário a uma chave
dinossauro2["peso"] = float(input("Digite o peso do dinossauro: "))
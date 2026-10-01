fila_refeitorio = []

def adicionar_estudante(fila):
    nome = input("Digite o nome do(a) estudante: ")
    fila.append(nome)
    print(f"{nome} foi adicionado(a) ao final da fila!")

def chamar_estudante(fila):
    if len(fila) != 0:
        nome = fila.pop(0)
        print(f"{nome} foi chamado(a)!")
    else:
        print("A fila está vazia!")

def exibir_fila(fila):
    if len(fila) != 0:
        print("\nFILA ATUAL:\n")
        for indice, nome in enumerate(fila):
            print(f"{indice+1}º - {nome}")
    else:
        print("A fila está vazia!")

def encontrar_posicao(fila):
    nome = input("Digite o nome de quem você procura na fila: ")
    achou = False
    for indice, pessoa in enumerate(fila):
        if pessoa == nome:
            print(f"{pessoa} está em {indice+1}º lugar na fila")
            achou = True
            break
    if not achou:
        print(f"{nome} não está na fila!")

print("Bem-vindos e bem-vindas ao refeitório!\n")
while True:
    print(""" MENU DE OPÇÕES 
          1 - Adicionar estudante
          2 - Chamar estudante
          3 - Exibir fila
          4 - Encontrar alguém na fila
          5 - Sair
""")
    escolha = int(input("Digite o número da sua opção: "))
    if escolha == 1:
        adicionar_estudante(fila_refeitorio)
    elif escolha == 2:
        chamar_estudante(fila_refeitorio)
    elif escolha == 3:
        exibir_fila(fila_refeitorio)
    elif escolha == 4:
        encontrar_posicao(fila_refeitorio)
    elif escolha == 5:
        print("Obrigado! Volte sempre.")
        break
    else:
        print("Opção inválida!")
while True:
    print("""
    1 - Somar
    2 - Subtrair
    3 - Sair
          """)
    opcao = int(input("Digite a sua opção: "))
    if opcao == 1:
        print("Vai somar")
    elif opcao == 2:
        print("Vai subtrair")
    elif opcao == 3:
        print("Vai sair")
        break
    else:
        print("Opção inválida!")

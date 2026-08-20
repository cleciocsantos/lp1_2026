tentativas = 5

while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == "1234":
        break
    print("Senha incorreta!")
    tentativas -= 1 # é o mesmo que tentativas = tentativas - 1
    print(f"Você tem mais {tentativas} tentativas!")

# Teste pra saber se saiu do while porque as tentativas acabaram ou porque acertou a senha
if tentativas == 0:
    print("Tentativas esgotadas. Tente mais tarde!")
else:
    print("Senha correta!")
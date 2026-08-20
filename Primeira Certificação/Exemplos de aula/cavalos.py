# Exercício: Ajude um aras a descobrir a quantidade de ferraduras necessárias para todos os seus cavalos.
# Informe também qual será o custo total das ferraduras. Sabendo que:
# De 0 a 50 ferraduras o custo unitário é R$ 15,00.
# Acima de 50 ferraduras o custo unitário é R$ 9,00.
 
cavalos = int(input("Digite  quantidade de cavalos: "))
ferraduras = cavalos * 4
print(f"Você vai precisar de {ferraduras} ferraduras")
if ferraduras > 50:
    preco = ferraduras * 9
else:
    preco = ferraduras * 15
print(f"O custo total será de R${preco:.2f}")
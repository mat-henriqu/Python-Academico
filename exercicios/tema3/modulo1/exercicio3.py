# calcular o preço de uma compra sendo o preço unitario  10
# ate 10 unidades nao ha desconto
# entre 11 e 20 desconto de 10%
# 21 pra cima desconto de 20%

precoUnitario = 10.00
DESCONTO10 = 0.90
DESCONTO20 = 0.80

quantidade = int(input("Digite a quantidade de itens que deseja comprar: "))
if quantidade <= 10:
    precoTotal = precoUnitario * quantidade
    print("TOTAL R$", precoTotal)
elif 10 <= quantidade <= 20:
    precoTotal = precoUnitario * quantidade * DESCONTO10
    print("TOTAL R$", precoTotal)
else:
    precoTotal = precoUnitario * quantidade * DESCONTO20
    print("TOTAL R$", precoTotal)

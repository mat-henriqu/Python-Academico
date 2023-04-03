# indicar reprovação ou aprovação
# >=7 aprovado
# >=5<7 recuperação
# <5 reprovado
nota = float(input("Digite sua nota "))

if nota>=7:
    print("Aprovado")
elif nota>=5:
    print ("Recuperação")
else:
    print("Reprovado")
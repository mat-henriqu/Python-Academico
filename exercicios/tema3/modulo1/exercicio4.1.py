# crie uma solução que some apenas numeros pares

lista = [10, 2, 5, 7, 6, 3]
n = len(lista)
soma = 0
for i in range(n):
    if lista[i] % 2 == 0:
        soma = soma + lista[i]
print(soma)

idade = []
altura = []

for i in range(0, 5, 1):
    idade.append(input("Digite sua idade: "))
    altura.append(input("Digite sua altura: "))
    

idadeInvertida = reversed(idade)
alturaInvertida = reversed(altura)

print("Idades invertidas: ")

for n in idadeInvertida: #O(n)
    print(n)


print("Alturas invertidas: ")

for n in alturaInvertida: #O(n)
    print(n)

#Complexidade da função reversed é O(n). Pois no pior caso precisa acessar todos os elementos da lista para poder inverte-la

#Nesse caso sabemos que a lista tem tamanho 5 e o porém mesmo em problemas simples é interessante analisar a complexidade.
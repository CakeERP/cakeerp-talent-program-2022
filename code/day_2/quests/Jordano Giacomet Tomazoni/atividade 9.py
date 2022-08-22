lista = []

for i in range(0, 3 ,1):
    lista.append(int(input("Digite um número: ")))

lista.sort(reverse=True) #O(n log n) -> Utiliza o tim sort sendo ele uma mesclagem entre o mergesort e o insertion sort

print("Lista ordenada em ordem decrescente: \n")

for n in lista:
    print(n)

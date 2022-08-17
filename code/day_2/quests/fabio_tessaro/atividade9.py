numeros = []

for i in range(3):
    num = input("Informe um número: ")
    numeros.append(num)


print("Em ordem decrescente: ")
numeros.sort(reverse = True)

print(numeros)
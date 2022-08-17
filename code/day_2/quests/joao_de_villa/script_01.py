# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

for i in range(5):
    numeros.append(int(input("Digite um número inteiro: ")))

print("Números digitados: ")
for i in range(len(numeros)):
    print(numeros[i])


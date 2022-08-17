# 2 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem
# lida.

idade = []
altura = []

for i in range(5):
    idade.append(int(input("Digite a idade da pessoa:")))
    altura.append(float(input("Digite a altura em metros da pessoa:")))

idade.reverse()
altura.reverse()

print("Idades revertidas: ")
for i in idade:
    print(i)

print("Alturas revertidas: ")
for i in altura:
    print(i)

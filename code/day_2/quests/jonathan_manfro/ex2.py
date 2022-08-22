idade = []
altura = []

for i in range(1,6):
    X = int(input("Digite a idade da pessoa: "))
    Y = float(input("Digite a altura da: "))
    idade.append(X)
    altura.append(Y)

print("Ordem inversa do vetor idade: ")
idade.reverse()
print(idade)
print("Altura inversa do vetor altura: ")
altura.reverse()
print(altura)
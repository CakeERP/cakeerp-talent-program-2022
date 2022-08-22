idade = []
altura = []

for i in range(1,6):
    print("Input dos valores")
    idades = int(input("Digite a idade de uma pessoa: "))
    alturas = float(input("Digite a altura dessa pessoa: "))
    idade.append(idades)
    altura.append(alturas)

print("Ordem Lida")
print("Idade em ordem reversa: ")
print(idade)
print("Altura em ordem reversa: ")
print(altura)
print("-------------------------")
print("Idade em ordem reversa: ")
idade.reverse()
print(idade)
print("Altura em ordem reversa: ")
altura.reverse()
print(altura)
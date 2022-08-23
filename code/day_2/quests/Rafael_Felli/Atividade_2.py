vet_altura = []
vet_idade = []

for i in range(0,5):
    vet_idade.append(int(input("Digite as idades: ")))

print("\n")
for i in range(0,5):
    vet_altura.append(float(input("Digite as alturas: ")))

print("\n A ordem original dos vetores eh: \n")
print(vet_idade)
print(vet_altura)

vet_altura.reverse()
vet_idade.reverse()

print("\n A ordem inversa dos vetores eh: \n")
print(vet_idade)
print(vet_altura)
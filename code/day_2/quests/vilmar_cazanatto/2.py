import os
from mydefs import inputAdapter       

people = []

for c in range(5):
    print(f'{c + 1}ª pessoa:')
    people.append({
        "age": inputAdapter(int, "Qual a idade? ", "Idade deve ser um número inteiro"),
        "height": inputAdapter(int, "Qual sua altura? (cm)", "Altura deve ser um número inteiro")
    })
    os.system('cls||clear')

for i, p in enumerate(reversed(people)):
    print(f'{5 - i}ª pessoa: {p["age"]} anos e {p["height"] /100}m')
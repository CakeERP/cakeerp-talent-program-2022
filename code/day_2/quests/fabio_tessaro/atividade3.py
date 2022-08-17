

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?",
    "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

print("Perguntas sobre o crime: Utilize 's' para Sim e 'n' para Não. ")

contador = 0

for indice, pergunta in enumerate(perguntas):
    pessoa = input(f"{indice + 1}) {perguntas[indice]} ")
    if pessoa == "s":
        contador = contador + 1

if contador == 5:
    print("A classificação da pessoa em relação ao crime é: Assassino")
elif contador <= 4 and contador >= 3:
    print("A classificação da pessoa em relação ao crime é: Cúmplice")
elif contador == 2:
    print("A classificação da pessoa em relação ao crime é: Suspeito")
else:
    print("A classificação da pessoa em relação ao crime é: Nulo")
        



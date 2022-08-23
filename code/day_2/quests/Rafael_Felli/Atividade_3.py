questions = {
    "a" : "Telefonou para a vítima?",
    "b" : "Esteve no local do crime?",
    "c" : "Mora perto da vítima?",
    "d" : "Devia para a vítima?",
    "e" : "Já trabalhou com a vítima?"
}

cont = 0
answer = ""

for i in questions:
    print(questions[i])
    answer = input("Responda com S ou N: ")
    print("\n")
    if answer == "S":
        cont += 1

if cont == 5:
    print("Assassino")
elif (cont == 3) or (cont == 4):
    print("Cumplice")
elif cont == 2:
    print("Suspeita")
else:
    print("Inocente")
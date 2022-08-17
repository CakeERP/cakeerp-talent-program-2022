# 3 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    # A. "Telefonou para a vítima?"
    # B. "Esteve no local do crime?"
    # C. "Mora perto da vítima?"
    # D. "Devia para a vítima?"
    # E. "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

respostas = []
true = 0
false = 0

print("Responda com S ou N - Qualquer resposta diferente de S ou N será considerada como N. ")
for p in perguntas:
    print(p)
    respostas.append(input())

for i in range(len(respostas)):
    if respostas[i].lower() == 's':
        true += 1

if (true == 2):
    print("Você foi classificado como SUSPEITO.")
elif (true == 3 or true == 4):
    print("Você foi classificado como CÚMPLICE.")
elif (true == 5):
    print("Você foi classificado como ASSASSINO.")
else:
    print("Você foi classificado como INOCENTE.")
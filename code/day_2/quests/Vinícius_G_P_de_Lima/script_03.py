perg= ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
resp=[]
positivo=0

print("Responda com S ou N")
for i in perg:
    print(i)
    resp.append(input())

for i in range(len(resp)):
    if resp[i].lower() == 's':
        positivo += 1

if (positivo == 2):
    print("SUSPEITO.")
elif (positivo == 3 or positivo == 4):
    print("CÚMPLICE.")
elif (positivo == 5):
    print("ASSASSINO.")
else:
    print("INOCENTE.")

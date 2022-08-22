perguntas = {
    "a" : "Telefonou para a vítima?",
    "b" : "Esteve no local do crime?",
    "c" : "Mora perto da vítima?",
    "d" : "Devia para a vítima?",
    "e" : "Já trabalhou com a vítima?"}

respostas = []
contador = 0


print("Digite s ou n respondendo as perguntas")

print(perguntas.get("a"))
respostas.append(input())
print(perguntas.get("b"))
respostas.append(input())
print(perguntas.get("c"))
respostas.append(input())
print(perguntas.get("d"))
respostas.append(input())
print(perguntas.get("e"))
respostas.append(input())

for x in range(5):
    if respostas[x] == "s": 
        contador += 1
 
if (contador == 2):
    print("Suspeita")
elif (contador == 3) or (contador == 4):
    print("Cúmplice")
elif (contador == 5):
    print("Assassino")
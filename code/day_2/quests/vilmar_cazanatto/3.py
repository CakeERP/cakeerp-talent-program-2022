import os
from mydefs import inputAdapter

def murdererClass(i):
    c = 0
    for i in interrogatory: c += 1 if i["a"] else 0
    if c == 2: return "Suspeito"
    if c == 5: return "Assassino"
    if c > 2: return "Cúmplice"
    return "Inocente"

interrogatory = [
    {"q": "Telefonou para a vítima? ", "a": False},
    {"q": "Esteve no local do crime? ", "a": False},
    {"q": "Mora perto da vítima? ", "a": False},
    {"q": "Devia para a vítima? ", "a": False},
    {"q": "Já trabalhou com a vítima? ", "a": False}
]

print("Interrogatório ((S)im ou (N)ão)")
for i in interrogatory:
    i["a"] = inputAdapter(bool, i["q"], "Responda com (S)im ou (N)ão")
    os.system('cls||clear')

print("Você responde que:")
for i in interrogatory:
    awnser = "" if i["a"] else "Não "
    awnser += i["q"] if i["a"] else i["q"].removeprefix("Já ") #Remove o Já quando Não
    awnser = awnser.replace("?", ".")
    awnser = "\t" + awnser.capitalize()
    print(awnser)

print(f'Classificando-o como: \n\t{murdererClass(interrogatory)}')
dicionario = {
    "A": "A - Telefonou para a vítima?",
    "B": "B - Esteve no local do crime?",
    "C": "C - Mora perto da vítima?",
    "D": "D - Devia para a vítima?",
    "E": "E - Já trabalhou com a vítima?",

}
print(dicionario.get("A"))
print(dicionario.get("B"))
print(dicionario.get("C"))
print(dicionario.get("D"))
print(dicionario.get("E"))

remover_itens = []

j = int(input("Quantas acusações falsas estão presentes na lista? "))

for i in range(j):
    r = str(input("Selecione as acusações falsas: "))
    remover_itens.append(r)

for item in remover_itens:
    dicionario.pop(item)

print(dicionario)
tamanhoDic = len(dicionario)
if tamanhoDic == 2:
    print("Você é suspeito!")
elif tamanhoDic > 2 and tamanhoDic <= 4:
    print("VC É CUMPLICE")
elif tamanhoDic >= 5:
    print("ASSASSINOOOOOOOO")
else:
    print("Liberado")
    
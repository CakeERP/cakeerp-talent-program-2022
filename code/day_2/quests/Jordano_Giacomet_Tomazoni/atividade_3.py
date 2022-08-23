lista = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

cont = 0

for n in lista: # O(n)
    print(f'{n}\n')
    resposta = input("Digite sim ou não: \n")
    print("")
    if resposta == "sim":
        cont+=1
    elif resposta == "não":
        continue


if cont == 2 :
    print("Suspeito!")
elif cont > 2 and cont < 5:
    print("Cúmplice")
elif cont == 5:
    print("Assassino!")
else:
    print("Inocente!")
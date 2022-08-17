# 7 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite um sexo (M/F):")

if (letra.lower() == "m"):
    print("Masculino")
elif (letra.lower() == "f"):
    print("Feminino")
else:
    print("Sexo inválido")
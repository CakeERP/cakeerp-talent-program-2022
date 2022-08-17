# 4 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

def soma(a,b,c):
    return a+b+c;

print("A soma dos termos resultou em:", soma(a,b,c))
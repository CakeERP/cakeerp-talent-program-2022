# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

maior = a
menor = a
meio = a

if (b > maior):
    maior = b

if (c > maior):
    maior = c

if (b < menor):
    menor = b

if (c < menor):
    menor = c

if ((b > a and b < c) or (b > c and b < a)):
    meio = b

if ((c > a and c < b) or (c > b and c < a)):
    meio = c

print("Maior:", maior)
print("Meio:", meio)
print("Menor:", menor)
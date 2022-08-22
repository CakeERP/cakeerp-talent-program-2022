sAtual = float(input("Digite seu salário atual: "))
sNovo = 0
vAumento = 0
percentual = 0

if (sAtual <= 280):
    sNovo = sAtual + (sAtual * 0.2)
    vAumento = sAtual * 0.2
    percentual = 20

elif (sAtual > 280 and sAtual <= 700):
    sNovo = sAtual + (sAtual * 0.15)
    vAumento = sAtual * 0.15
    percentual = 15
elif (sAtual > 700 and sAtual <= 1500):
    sNovo = sAtual + (sAtual * 0.1)
    vAumento = sAtual * 0.1
    percentual = 10
else:
    sNovo = sAtual + (sAtual * 0.05)
    vAumento = sAtual * 0.05
    percentual = 5

print("O antigo salário: ", sAtual)
print("O novo salário: ", sNovo)
print(" O valor do aumento: ", vAumento)
print("Porcentagem : ", percentual)
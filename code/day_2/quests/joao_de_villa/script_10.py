# 10 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que
# calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
# atual:
    # A. salários até R$ 280,00 (incluindo) : aumento de 20%
    # B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # D. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    # E. o salário antes do reajuste;
    # F. o percentual de aumento aplicado;
    # G. o valor do aumento;
    # H. o novo salário, após o aumento.


salarioAtual = float(input("Digite seu salário atual: "))
salarioNovo = 0
percentual = 0
valorAumento = 0

if (salarioAtual <= 280):
    salarioNovo = salarioAtual + (salarioAtual * 0.2)
    valorAumento = salarioAtual * 0.2
    percentual = 20
elif (salarioAtual > 280 and salarioAtual <= 700):
    salarioNovo = salarioAtual + (salarioAtual * 0.15)
    valorAumento = salarioAtual * 0.15
    percentual = 15
elif (salarioAtual > 700 and salarioAtual <= 1500):
    salarioNovo = salarioAtual + (salarioAtual * 0.1)
    valorAumento = salarioAtual * 0.1
    percentual = 10
else:
    salarioNovo = salarioAtual + (salarioAtual * 0.05)
    valorAumento = salarioAtual * 0.05
    percentual = 5

print("Salário Antigo: ", salarioAtual)
print("Salário novo: ", salarioNovo)
print("Valor do aumento: ", valorAumento)
print("Porcentagem do aumento: ", percentual)


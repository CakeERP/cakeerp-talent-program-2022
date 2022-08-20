salario = float(input("Digite o salario do funcionario: "))

novo_salario = 0
percentual = 0
aumento = 0

if salario > 1500:
    novo_salario = salario * 1.05
    percentual = 5
    aumento = salario * 0.05
elif (salario > 700) and (salario <= 1500):
    novo_salario = salario * 1.10    
    percentual = 10
    aumento = salario * 0.10
elif (salario > 280) and (salario <= 700):
    novo_salario = salario * 1.15
    percentual = 15
    aumento = salario * 0.15
else:
    novo_salario = salario * 1.20
    percentual = 20
    aumento = salario * 0.2

print(f'\nO salario antes do reajuste era: R${round(salario, 2)}')
print(f'O percentual de aumento aplicado foi: {percentual} %')
print(f'O valor do aumento foi de: R${round(aumento, 2)}')
print(f'O novo salario apos o aumento eh de: R${round(novo_salario, 2)}')
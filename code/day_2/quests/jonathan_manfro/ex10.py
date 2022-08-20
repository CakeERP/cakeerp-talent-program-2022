salario = float(input("Digite o salário do colaborador\n"))
aumento = 0
salarioAlmento = 0
porcentagem = 0
if (salario < 280):
    aumento = (salario * 20) / 100
    salarioAumento = salario + aumento
    porcentagem = 20
elif((salario >= 280) and (salario < 700)):
    aumento = (salario * 15) / 100
    salarioAumento = salario + aumento
    porcentagem = 15
elif((salario >= 700) and (salario < 1500)):
    aumento = (salario * 10) / 100
    salarioAumento = salario + aumento
    porcentagem = 10
else:
    aumento = (salario * 5) / 100
    salarioAumento = salario + aumento
    porcentagem = 5

aumento = round(aumento, 2)
salarioAumento = round(salarioAumento, 2)
salario = round(salario, 2)


print('Salário antes do aumento: R$' + str(salario))
print('O aumento foi de: R$' + str(aumento))
print('A porcentagem é de:'+ str(porcentagem)+' %')
print('O reajuste do salário foi para: R$ ' + str(salarioAumento))
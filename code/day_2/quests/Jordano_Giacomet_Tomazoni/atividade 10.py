salario = float(input("Digite o salário do colaborador: "))
salarioFinal = 0
reajuste = 0
aumento = 0

if(salario < 280): # Caso fosse um sistema orientado a objetos acredito que poderiamos usar o padrão chain of responsability
    reajuste = 20
    aumento = salario * (reajuste / 100)
    salarioFinal = salario + aumento
elif(salario >= 280 and salario < 700):
    reajuste = 15
    aumento = salario * (reajuste / 100)
    salarioFinal = salario + aumento
elif(salario >= 700 and salario < 1500):
    reajuste = 10
    aumento = salario * (reajuste / 100)
    salarioFinal = salario + aumento
else:
    reajuste = 5
    aumento = salario * (reajuste / 100)
    salarioFinal = salario + aumento

print("Resultado Final: \n")
print(f'O salário inicial é: {salario}\n')
print(f'O percentual de aumento é: {reajuste}\n')
print(f'O valor do aumento é: {aumento}\n')
print(f'O novo salário é: {salarioFinal}\n')
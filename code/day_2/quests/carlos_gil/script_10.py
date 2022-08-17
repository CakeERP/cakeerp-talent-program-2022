salario = int(input("Digite o seu salário: "))

print("Antes Reajuste: ", salario)

salMin = salario * 0.2
ajusteMin = salario * 1.2
salMed = salario * 0.15
ajusteMed = salario * 1.15
salAlto = salario * 0.1
ajusteAlto = salario * 1.1
salMax = salario * 0.05
ajusteMax = salario * 1.05


if salario <= 280: 
    print("Aumento de 20%, valor do aumento: ", salMin)
    print("salário após reajuste: ", ajusteMin)
elif salario > 200 and salario <= 700: 
    print("Aumento de 15% valor do aumento: ", salMed) 
    print("salário após reajuste: ", ajusteMed)
elif salario > 700 and salario <= 1500: 
    print("Aumento de 10% valor do aumento: ", salAlto)
    print("salário após reajuste: ", ajusteAlto)
else: 
    print("Aumento de 5% valor do aumento: ", salMax)
    print("salário após reajuste: ", ajusteMax)
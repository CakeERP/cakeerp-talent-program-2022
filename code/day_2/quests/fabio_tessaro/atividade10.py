salario_antigo = float(input("Informe seu salário: R$"))
salario_novo = float(0)

aumento = float(0)

if salario_antigo <= 280.00:
    aumento = (salario_antigo/100) * 20
    salario_novo = salario_antigo + aumento
    print(f"Salário antes do reajuste: R${salario_antigo}")
    print("O percentual de aumento foi de 20%")
    print(f"O valor do aumento foi de: R${aumento}")
    print(f"Salário após reajuste: R${salario_novo}")
    

elif salario_antigo > 280.00 and salario_antigo <= 700.00:
    aumento = (salario_antigo/100) * 15
    salario_novo = salario_antigo + aumento
    print(f"Salário antes do reajuste: R${salario_antigo}")
    print("O percentual de aumento foi de 15%")
    print(f"O valor do aumento foi de: R${aumento}")
    print(f"Salário após reajuste: R${salario_novo}")

elif salario_antigo > 700.00 and salario_antigo <= 1500.00:
    aumento = (salario_antigo/100) * 10
    salario_novo = salario_antigo + aumento
    print(f"Salário antes do reajuste: R${salario_antigo}")
    print("O percentual de aumento foi de 10%")
    print(f"O valor do aumento foi de: R${aumento}")
    print(f"Salário após reajuste: R${salario_novo}")

else:
    aumento = (salario_antigo/100) * 5
    salario_novo = salario_antigo + aumento
    print(f"Salário antes do reajuste: R${salario_antigo}")
    print("O percentual de aumento foi de 5%")
    print(f"O valor do aumento foi de: R${aumento}")
    print(f"Salário após reajuste: R${salario_novo}")


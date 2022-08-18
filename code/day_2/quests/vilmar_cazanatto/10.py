import os
from mydefs import inputAdapter

def getIncrease(salary):
    if salary <= 280: return .2
    if salary < 700: return .15
    if salary < 1500: return .1
    return .05

print("Calcular novo salário:")
s = inputAdapter(float, "Digite seu salário atual: R$", "Salário deve ser um número")
p = getIncrease(s)
os.system('cls||clear')

print(f'Salário antes do reajuste:      R${"%.2f" % s}')
print(f'Percentual de aumento aplicado: {int(p * 100)}%')
print(f'Valor do aumento:               R${"%.2f" % round( p * s, 2)}')
print(f'Novo salário, após o aumento:   R${"%.2f" % round( s * (p + 1), 2)}')
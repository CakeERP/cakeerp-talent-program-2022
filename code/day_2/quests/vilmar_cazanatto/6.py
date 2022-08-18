from mydefs import inputAdapter

print("Digite dois números")
n1 = inputAdapter(float, "1º número: ", "Precisa ser um número (Ex. 1; 2.4; -4; 0.007)")
n2 = inputAdapter(float, "2º número: ", "Precisa ser um número (Ex. 1; 2.4; -4; 0.007)")

n1 = int(n1) if round(n1) == n1 else n1
n2 = int(n2) if round(n2) == n2 else n2

if n1 == n2: print("Os números iguais.")
else: print(f'O maior é: {n1 if n1 > n2 else n2}')
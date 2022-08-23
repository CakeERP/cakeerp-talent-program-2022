numeros = []

for i in range(3):
    i = int(input(f'Digite o {i+1} numero: '))
    numeros.append(i)

numeros.sort(reverse = True)
print("Os numeros na ordem descrescente sao: " + str(numeros)[1:-1])
letra = input(("Digite M ou F: \n"))

if(letra.upper() == 'M'):
    print(f'M - Masculino')
elif(letra.upper() == 'F'):
    print(f'F - Feminino')
else:
    print("Sexo Inválido")
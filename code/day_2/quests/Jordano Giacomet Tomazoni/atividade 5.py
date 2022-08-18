def somaImposto(taxaImposto, custo):
    return ((taxaImposto/100) * custo) + custo #Considerando que a taxa vai ser escrita como por exemplo 5%, 10%

print(f'O custo final é: {somaImposto(5, 100)}')
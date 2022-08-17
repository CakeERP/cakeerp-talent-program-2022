def somaImposto(taxaImposto, custo):
    return round((custo + custo*(taxaImposto/100)), 2)


custo = float(input("Digite o custo: "))
taxa = float(input("Digite a porcentagem da taxa: "))

print("O custo modificado é igual a: ", somaImposto(taxa, custo))

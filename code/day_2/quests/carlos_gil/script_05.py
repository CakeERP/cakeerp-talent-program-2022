def somaImposto(taxaImposto, custo):
    return (1 + taxaImposto / 100) * custo
taxa = float(input('Digite a taxa: '))
cst = float(input('Digite o custo: '))
print('Valor com imposto:', somaImposto(taxa,cst))
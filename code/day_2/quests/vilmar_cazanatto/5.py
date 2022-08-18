def somaImposto(taxaImposto, custo): return round(custo * (1 + taxaImposto / 100), 2)

print(f'Um produto que custa $26.50 com imposto de 13% custara ${"%.2f" % somaImposto(13, 26.5)}')
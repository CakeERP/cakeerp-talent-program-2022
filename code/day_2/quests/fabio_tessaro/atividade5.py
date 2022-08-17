

def somaImposto(taxaImposto, custo):
    imposto = float(taxaImposto/100)
    valor_alterado = custo + imposto
    print(valor_alterado)


somaImposto(50, 3)
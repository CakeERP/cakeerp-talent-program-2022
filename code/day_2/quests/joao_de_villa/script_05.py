# 5 - Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

custo = float(input("Digite o custo: "))
taxa = float(input("Digite a taxa em porcentagem: "))

def somaImposto(taxaImposto, custo):
    return round((custo + custo*(taxaImposto/100)), 2)

print("O custo com os impostos fica: ", somaImposto(taxa, custo), "R$")
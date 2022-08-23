def somaImposto(taxaImposto,custo):
    custo *= (taxaImposto / 100) + 1
    print("O novo custo do produto incluindo imposto sera: " + str(custo))

x = int(input("Digite o imposto em porcentagem: "))
y = int(input("Digite o custo do produto: "))
somaImposto(x,y)
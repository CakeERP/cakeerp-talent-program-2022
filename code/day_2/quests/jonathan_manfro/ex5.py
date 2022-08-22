def somaImposto (taxaImpostos, custo):
    produto = (custo * taxaImpostos) / 100
    print(produto + custo)

x = float(input("Qual o preço do produto sem impostos?"))
y = float(input("Qual a taxa de impostos sobre o produto?"))
somaImposto(y, x)
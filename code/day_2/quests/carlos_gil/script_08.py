a = input('Digite sua nota: ')
b = input('Digite sua 2° nota: ')

media = (a + b) / 2

if media >= 7 and media < 10:     
    print("Você foi Aprovado")
elif media >= 10:
    print("Aprovado com Distinção")
else:
    print("Infelizmente você foi reprovado")
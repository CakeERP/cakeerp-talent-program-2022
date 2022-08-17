n1= float(input("Digite a primeira nota: "))
n2= float(input("Digite a segunda nota: "))

media=(n1+n2)/2

if(media == 10):
    print("APROVADO COM DISTINÇÃO")
elif (media >= 7):
    print("APROVADO")
elif(media < 7):
    print("REPROVADO")

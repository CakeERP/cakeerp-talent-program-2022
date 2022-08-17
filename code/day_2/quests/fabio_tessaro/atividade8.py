
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aluno Aprovado com Distinção!")
elif media >= 7:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")
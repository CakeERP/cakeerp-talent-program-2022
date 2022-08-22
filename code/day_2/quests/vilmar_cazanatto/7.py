def selectGenre(genre):
    if genre == "F": return "Feminino"
    if genre == "M": return "Masculino"
    return "Sexo Inválido"

print(selectGenre(input("Digite seu sexo: (F)eminino (M)asculino\n")))
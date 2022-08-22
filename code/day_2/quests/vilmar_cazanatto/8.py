from typing import final
from mydefs import inputAdapter

def isApproved(final_grade):
    if final_grade == 10: return "Aprovado com Distinção"
    if final_grade >= 7: return "Aprovado"
    return "Reprovado"

print("Informe as notas do aluno:")

avg = round(
    (inputAdapter(float, "1ª nota: ", "Nota deve ser um número") +
    inputAdapter(float, "2ª nota: ", "Nota deve ser um número")) 
    / 2, 2)


print(f'A média final foi: {avg}\n{isApproved(avg)}')
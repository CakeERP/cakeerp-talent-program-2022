from pickle import FALSE, TRUE
from mydefs import inputAdapter

nums = []


print("Digite 3 números:")

for c in range(3):
    n = inputAdapter(float, f'{c + 1}º número: ', "Digite apenas números.")
    nums.append(int(n) if round(n) == n else n )

nums.sort(reverse=True)
print(f'Em ordem decrescente: \n{nums}')
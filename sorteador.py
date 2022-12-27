from random import randint
num_max = 28
num_sorteados = []

while len(num_sorteados) < num_max:
    num_sorteado = randint(1, num_max)
    if num_sorteado not in num_sorteados:
        num_sorteados.append(num_sorteado)

print(num_sorteados)
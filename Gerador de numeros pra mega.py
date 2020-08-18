# Gerador de numeros para quem quer apostar megasena.

from random import sample
from time import sleep

jogos = list()
n = int(input('Quantos jogos vc quer jogar ?: '))
for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a[:])
    print(f' jogo {c + 1}: {a}')
    sleep(0.85)

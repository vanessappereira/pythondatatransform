# Introduction into Numpy

import numpy as np

numeros = [2, 4, 6, 8, 10]

# Para calcular a média com o Numpy
media = np.mean(numeros)
print(f"A média dos números do array é: {media}")

# Para calcular a mediana com o Numpy
mediana = np.median(numeros)
print(f"A média dos números do array é: {mediana}")

# Para calcular o desvio padrão com o Numpy
dPadrao = round(np.std(numeros), 4)
print(f"O desvio padrão dos números do array é: {dPadrao}")

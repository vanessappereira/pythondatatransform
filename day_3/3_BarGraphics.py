# Introduction into MatPlotLib

import matplotlib.pyplot as plt

# 1st example with a graphic bar
frutas = ["Bananas", "Maçãs", "Laranjas", "Tangerinas"]
quant = [4, 6, 8, 6]

plt.bar(frutas, quant)
plt.xlabel("Frutas")
plt.ylabel("Quantidade")
plt.title("Gráfico de Barras")
plt.show()

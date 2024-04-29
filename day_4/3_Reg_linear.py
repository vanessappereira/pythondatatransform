import matplotlib.pylot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6];
y = [2, 3, 4, 5, 6, 7];

m, b = np.polyfit(x, y, 1);

plt.scatter(x, y, color="green", label="Dados");
plt.plot(x, m * x + b, color='red', label='Regressão Linear');

plt.xlabel("Eixo X");
plt.ylabel("Eixo Y");
plt.title("Gráfico de Regressão Linear");

plt.show();

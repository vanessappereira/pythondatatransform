import matplotlib as plt;
import numpy as np;

dados = np.random.normal(loc=0,scale=1,size=100);
mediana = np.median(dados);

plt.hist(dados, bin=20, alpha=0.5, color='blue', edgecolor='black');
plt.axvline(mediana, color='red', linestyle='dashed', linewidth=1);

plt.xlabel('Valores');
plt.ylabel('Frequência');
plt.title('Histograma com mediana');

plt.show();
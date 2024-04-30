# Criar 3 exemplos de gráficos que gerem vários tipos de dados através de array.

import matplotlib.pyplot as plt
import numpy as np


# Gráfico circular
def grafCircular():
    tarefas = [
        "Aspirar a casa",
        "Lavar loiça",
        "Passar a ferro",
        "Fazer as camas",
        "Limpar quintal",
        "Comida aos animais",
    ]
    tempoEstimado = [30, 15, 45, 20, 60, 10]
    # Criar o gráfico circular
    plt.pie(tempoEstimado, labels=tarefas, autopct="%1.1f%%")

    # Títulos e rótulos
    plt.title("Tempo estimado em cada tarefa")

    # Mostrar o gráfico
    plt.show()


# Gráfico com histograma mediana
# Baleias de borracha que cada nadador agarra na piscina
def grafHistMediana():
    nomes = ["Alberto", "Lucas", "Narcisa", "Helena", "Francisca", "Filipe"]
    valores = [7, 3, 5, 6, 8, 10]

    # Cálculo da mediana
    mediana = np.median(valores)

    # Criar o histograma
    plt.barh(nomes, valores, alpha=0.5, color="blue", edgecolor="black")

    # Adicionar uma linha vertical para a mediana
    plt.axvline(mediana, color="red", linestyle="dashed", linewidth=1)

    # Títulos e rótulos
    plt.title("Histograma da Mediana")
    plt.xlabel("Qtd de Baleias de borracha")
    plt.ylabel("Nomes")

    # Mostrar o gráfico
    plt.show()


def main():
    # grafCircular();
    grafHistMediana()


main()

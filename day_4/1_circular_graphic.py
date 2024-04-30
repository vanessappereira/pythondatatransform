import matplotlib.pyplot as plt

# Gráfico circular

frutas = ["Maçãs", "Bananas", "Pêras", "Laranjas"]
quantidades_vendidas = [20, 25, 15, 40]

plt.pie(quantidades_vendidas, labels=frutas, autopct="%1.1f%%")
plt.title("Gráfico Circular")
plt.show()

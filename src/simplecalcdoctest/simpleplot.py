import matplotlib.pyplot as plt

def plot_grafico_linear(x, y, xlabel="X", ylabel="Y", title="Gráfico Linear"):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_grafico_de_dispersao(x, y, xlabel="X", ylabel="Y", title="Gráfico de Dispersão"):
    plt.scatter(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_grafico_de_barra(x, y, xlabel="X", ylabel="Y", title="Gráfico de Barra"):
    plt.bar(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_grafico_de_pizza(labels, sizes, title="Gráfico de Pizza"):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Assegura que o gráfico de pizza é desenhado como um círculo.
    plt.title(title)
    plt.show()

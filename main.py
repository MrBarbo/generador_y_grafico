import matplotlib.pyplot as plt

def graficar_arreglo(datos):
    # Crea el gráfico de dispersión
    plt.scatter(range(len(datos)), datos)
    # Añade los nombres de los ejes y del gráfico
    plt.xlabel('Indice')
    plt.ylabel('Valor')
    plt.title('Gráfico de arreglo aleatorio')
    # Muestra el gráfico
    plt.show()

def generador():
    return lista

#print(generador(42723, 23436753, 12345, 100,20))
#graficar_arreglo(generador(42723, 23436753, 12345, 100,20))



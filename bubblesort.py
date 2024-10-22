import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

class Quicksort:
    def __init__(self):
        self.numeros = []
    
    def ordenar(self, valores):
        if valores is None or len(valores) == 0:
            return
        self.numeros = valores
        self.quicksort(0, len(valores) - 1)
    
    def quicksort(self, bajo, alto):
        i = bajo
        j = alto
        pivote = self.numeros[bajo + (alto - bajo) // 2]
        while i <= j:
            while self.numeros[i] < pivote:
                i += 1
            while self.numeros[j] > pivote:
                j -= 1
            if i <= j:
                self.intercambiar(i, j)
                i += 1
                j -= 1
        if bajo < j:
            self.quicksort(bajo, j)
        if i < alto:
            self.quicksort(i, alto)
    
    def intercambiar(self, i, j):
        self.numeros[i], self.numeros[j] = self.numeros[j], self.numeros[i]

def medir_tiempo_promedio_bubble_sort(tamaño_arreglo, iteraciones=10):
    tiempos = []
    for iteracion in range(iteraciones):
        arreglo = []
        for indice in range(tamaño_arreglo):
            arreglo += [random.randint(0, 1000000)]
        start_time = time.time()
        bubble_sort(arreglo)
        tiempos.append(time.time() - start_time)
    return sum(tiempos) / iteraciones

def medir_tiempo_promedio_quick_sort(tamaño_arreglo, iteraciones=10):
    tiempos = []
    for iteracion in range(iteraciones):
        arreglo = []
        for indice in range(tamaño_arreglo):
            arreglo += [random.randint(0, 1000000)]
        qs = Quicksort()
        start_time = time.time()
        qs.ordenar(arreglo)
        tiempos.append(time.time() - start_time)
    return sum(tiempos) / iteraciones

tamaños = [1000, 2000, 3000, 4000, 5000] 
tiempos_bubble = []
tiempos_quick = []

for tamaño in tamaños:
    tiempo_promedio_bubble = medir_tiempo_promedio_bubble_sort(tamaño)
    tiempos_bubble.append(tiempo_promedio_bubble)
    print(f"Tiempo promedio Bubble Sort: {tiempo_promedio_bubble:.5f} segundos")
    
    tiempo_promedio_quick = medir_tiempo_promedio_quick_sort(tamaño)
    tiempos_quick.append(tiempo_promedio_quick)
    print(f"Tiempo promedio QuickSort: {tiempo_promedio_quick:.5f} segundos")

def Graficar(tamaños,tiempo,nombre,colores):
    plt.plot(tamaños, tiempo, marker='o', linestyle='-', color=colores, label=nombre)
    plt.title('Comparación de tiempos de ejecución: ' + nombre)
    plt.xlabel('Tamaño del arreglo (n)')
    plt.ylabel('Tiempo promedio de ejecución (segundos)')
    plt.grid(True)
    plt.legend()
    plt.show()

Graficar(tamaños,tiempos_quick,"quicksort", "g")
Graficar(tamaños,tiempos_bubble,"bubblesort", "b")


# Graficar los resultados
plt.plot(tamaños, tiempos_bubble, marker='o', linestyle='-', color='b', label='Bubble Sort')
plt.plot(tamaños, tiempos_quick, marker='o', linestyle='-', color='g', label='QuickSort')
plt.title('Comparación de tiempos de ejecución: Bubble Sort vs QuickSort')
plt.xlabel('Tamaño del arreglo (n)')
plt.ylabel('Tiempo promedio de ejecución (segundos)')
plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt


# Creamos un array con la estatura de 18 estudiantes
estaturas = np.array([1.88,1.60, 1.60,1.60, 1.60, 1.60, 1.65, 1.59, 1.75, 1.59, 1.72, 1.74, 1.80, 1.61, 1.75, 1.69, 1.59, 1.66])

# Matriz de 2 dimensiones
estaturas = estaturas.reshape(-1, 1)

# Calculamos la media, mediana y desviación estándar
media = np.mean(estaturas)
mediana = np.median(estaturas)
desviacion_estandar = np.std(estaturas)

# Mostramos los resultados
print("Estaturas de los estudiantes:")
print(estaturas)
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)

plt.imshow (estaturas, cmap = "terrain", aspect='auto') 
plt.colorbar (label = "Estatura (m)")
plt.show ()

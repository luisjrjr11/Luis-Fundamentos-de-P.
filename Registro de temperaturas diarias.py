import numpy as np

# Ciudades de Ecuador
ciudades = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Tena", "Puyo"]

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Semanas
semanas = 4

# Crear matriz 3D
temperaturas = np.random.randint(10, 30, size=(len(ciudades), len(dias), semanas))

# Iterar sobre ciudades
for i in range(len(ciudades)):

    # Iterar sobre semanas
    for j in range(semanas):

        suma_temperaturas = 0
        num_dias = 0

        # Iterar sobre días
        for k in range(len(dias)):

            # Acumular temperaturas
            suma_temperaturas += temperaturas[i,k,j]
            num_dias += 1

        # Calcular promedio
        promedio = suma_temperaturas / num_dias

        # Imprimir resultados
        print(f"Promedio semana {j+1} en {ciudades[i]}: {promedio:.2f}")

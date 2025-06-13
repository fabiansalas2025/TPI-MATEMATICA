# TPI 2 MATEMATICA: Análisis de DNIs y Años de nacimiento
from datetime import datetime
from itertools import product

# PARTE A: Análisis de DNIs:

# 1. Solicita los DNIs al usuario, valida que sean numéricos y los almacena en una lista.
def pedir_dnis(): # Solicita DNIs al usuario y los almacena en una lista

    cantidad = 0 # Almacena la cantidad de DNIs a ingresar
    while cantidad < 1: # Asegura que se ingrese al menos un DNI y se inicia el bucle
        try:
            cantidad = int(input("Cantidad de DNIs a ingresar: ")) # Solicita la cantidad de DNIs
        except ValueError: # Captura el error si no se ingresa un número válido
            print("Debe ingresar un número válido.") # Si no es un número, solicita nuevamente

    lista_dnis = [] #Se crea la lista de DNIs
    for i in range(cantidad): # Bucle para solicitar cada DNI, se asegura que el DNI sea un número y no esté vacío y si no es válido, solicita nuevamente
        while True:
            dni = input(f"DNI {i + 1}: ").strip() # Con .strip() eliminamos espacios al inicio y al final
            if dni.isdigit(): # Verifica si el DNI es un numero
                lista_dnis.append(dni) # Si es un numero, lo agrega a la lista
                break
            else:
                print("Solo se aceptan números.") # Si el DNI no es un número, solicita nuevamente  
    return lista_dnis

# 2. Genera una lista de conjuntos, donde cada conjunto contiene los dígitos únicos de cada DNI.
def conjuntos_digitos_unicos(dnis): 
    return [set(map(int, dni)) for dni in dnis]

# 3. Muestra la unión, intersección, diferencia y diferencia simétrica entre los conjuntos de dígitos únicos de los DNIs.
def mostrar_operaciones_conjuntos(conjuntos):
    # Unión de todos los conjuntos
    union_total = set().union(*conjuntos)
    print("\nUnión total:", union_total) 

    # Intersección de todos los conjuntos
    interseccion_total = set.intersection(*conjuntos)
    print("Intersección total:", interseccion_total)

    # Diferencia entre pares de conjuntos
    print("\nDiferencias entre conjuntos:")  # Imprime un título para la sección de diferencias
    for i, ci in enumerate(conjuntos):  # Itera sobre cada conjunto con su índice
        for j, cj in enumerate(conjuntos):  # Itera nuevamente sobre cada conjunto con su índice
            if i < j:  # Solo compara cada par una vez y evita comparar un conjunto consigo mismo
                diferencia = ci - cj  # Calcula la diferencia de conjuntos (elementos en ci que no están en cj)
                print(f"Conjunto {i+1} ({ci}) - Conjunto {j+1} ({cj}): {diferencia if diferencia else ' - (conjunto vacío)'}")  # Muestra el resultado 

    # Diferencia simétrica entre pares de conjuntos
    print("\nDiferencias simétricas:")  # Imprime un título para la sección de diferencias simétricas
    for i, ci in enumerate(conjuntos):  # Itera sobre cada conjunto con su índice
        for j, cj in enumerate(conjuntos):  # Itera nuevamente sobre cada conjunto con su índice
            if i < j:   # Solo compara cada par una vez y evita comparar un conjunto consigo mismo
                diferencia_sim = ci ^ cj  # Calcula la diferencia simétrica (elementos en ci o cj pero no en ambos)
                print(f"Conjunto {i+1} ({ci}) - Conjunto {j+1} ({cj}): {diferencia_sim if diferencia_sim else ' - (conjunto vacío)'}")  # Muestra el resultado 

# 4. Cuenta y muestra la frecuencia de cada dígito (0-9) en todos los DNIs ingresados.
def frecuencia_digitos(dnis):  # Define una función que recibe la lista de DNIs
    conteo = [0]*10  # Inicializa una lista de 10 ceros para contar cada dígito del 0 al 9
    for dni in dnis:  # Itera sobre cada DNI en la lista
        for d in dni:  # Itera sobre cada dígito del DNI (como string)
            conteo[int(d)] += 1  # Convierte el dígito a entero y suma 1 en la posición correspondiente
    print("\nFrecuencia de dígitos:")  # Imprime un título para la sección de frecuencias
    for i, cant in enumerate(conteo):  # Itera sobre cada dígito y su cantidad
        print(f"Dígito {i}: {cant} veces")  # Muestra cuántas veces apareció cada dígito

# 5. Calcula y muestra la suma total de todos los dígitos de todos los DNIs.
def suma_total_digitos(dnis):  # Define una función que recibe la lista de DNIs
    total = sum(int(d) for dni in dnis for d in dni)  # Suma todos los dígitos de todos los DNIs
    print("\nSuma total de todos los dígitos:", total)  # Imprime el resultado

# 6. Evalúa si hay valores comunes en todos los conjuntos y si el grupo es equilibrado entre conjuntos de tamaño par e impar.
def evaluar_valores_y_equilibrio(conjuntos):  # Define una función que recibe la lista de conjuntos
    # Intersección entre todos los conjuntos
    comunes = set.intersection(*conjuntos)  # Calcula la intersección de todos los conjuntos (elementos comunes)
    if comunes:  # Si hay elementos comunes
        print("\nValores presentes en todos los conjuntos:", comunes)
    else:
        print("\nNo hay valores comunes en todos los conjuntos.")

    # Comparación entre cantidad de conjuntos con tamaño par e impar
    pares = sum(1 for c in conjuntos if len(c) % 2 == 0)
    impares = len(conjuntos) - pares
    if pares == impares:
        print("Grupo equilibrado entre pares e impares.")
    else:
        print("Grupo NO equilibrado.")

# PARTE B: Años de nacimiento 

# 7. Determina si un año dado es bisiesto.
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# 8. Solicita los años de nacimiento, calcula estadísticas y muestra el producto cartesiano entre años y edades.
def procesar_anios():
    cantidad = int(input("\nCantidad de integrantes: "))
    anios = []
    for i in range(cantidad):
        anio = int(input(f"Año de nacimiento {i+1}: "))
        anios.append(anio)

    # Estadísticas
    pares = sum(1 for a in anios if a % 2 == 0)
    impares = cantidad - pares
    hay_bisiesto = any(es_bisiesto(a) for a in anios)
    todos_z = all(a > 2000 for a in anios)

    # Resultados
    print(f"\nNacidos en año par: {pares}")
    print(f"Nacidos en año impar: {impares}")
    if todos_z:
        print("Grupo Z")
    if hay_bisiesto:
        print("Al menos un año bisiesto presente")

    # Cálculo de edades
    edades = [datetime.now().year - a for a in anios]

    # Producto cartesiano entre años y edades
    print("\nProducto cartesiano entre años y edades:")
    for par in product(anios, edades):
        print(par)

# --- Ejecución principal --- #

if __name__ == "__main__":
    # Parte A: análisis de DNIs
    dnis = pedir_dnis()
    conjuntos = conjuntos_digitos_unicos(dnis)

    mostrar_operaciones_conjuntos(conjuntos)
    frecuencia_digitos(dnis)
    suma_total_digitos(dnis)
    evaluar_valores_y_equilibrio(conjuntos)

    # Parte B: análisis de años de nacimiento
    procesar_anios()


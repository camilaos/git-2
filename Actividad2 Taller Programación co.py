def Menu():
    while True:
        print("Trabajo Práctico 2")
        opc = int(input("Ingrese un ejercicio del 1 al 10: "))
        if opc == 1:
            ejercicio1()

        elif opc == 2:
            ejercicio2()

        elif opc == 3:
            ejercicio3()

        elif opc == 4:
            ejercicio4()

        elif opc == 5:
            ejercicio5()

        elif opc == 6:
            ejercicio6()

        elif opc == 7:
            ejercicio7()

        elif opc == 8:
            ejercicio8()

        elif opc == 9:
            ejercicio9()
        
        elif opc == 10:
            ejercicio10()
        
        else:
            print("Opción no válida")

def ejercicio1():
    while True:
        try:
            num_entero = int(input("Ingrese un número entero: "))
            break
        except:
            print("Debe ingresar un número entero")

    print(f"La cantidad de digitos de {num_entero} son: {calculo_digitos_ent(num_entero)}")

def ejercicio2():
    while True:
        try:
            copia = float(input("Ingrese un número decimal: "))
            num_decimal = copia
            break
        except ValueError:
            print("Debe ingresar un número decimal")
    num_entero = int(copia)
    print(f"Cantidad de dígitos enteros: {calculo_digitos_ent(num_entero)}. Cantidad de dígitos decimales: {calculo_digitos_dec(num_decimal)}") 

def ejercicio3():
    while True:
        try:
            vector = []
            cantidad_num = int(input("Ingrese la cantidad de números que desea ingresar: "))

            for i in range(0,cantidad_num):
                num = int(input("Ingrese un número: "))
                
                if num != 0:
                    cargar_compuestos(num,vector)
                else:
                    break
        except ValueError:
            print("No puede haber un vector con ese tipo de dato.")
        
        print(f"Vector con números compuestos: {vector}")

def ejercicio4():
    while True:
        try:
            vector = []
            N = int(input("Ingrese la cantidad de números que desea ingresar: "))

            for i in range(N):
                numeros = int(input(f"Ingrese un número: "))
                vector.append(numeros)
            print(f"Vector original: {vector}")

            vector_invertido_auxiliar = invertir_con_auxiliar(vector)
            print(f"Vector invertido con auxiliar: {vector_invertido_auxiliar}")

            vector_sin_auxiliar = invertir_sin_auxiliar(vector)
            print(f"Vector invertido sin auxiliar: {vector_sin_auxiliar}")

        except ValueError:
            print("No puede haber un vector con ese tipo de dato.")

def ejercicio5():
    while True:
        try:
            lista_A = []
            N = int(input("Ingrese la cantidad de números que desea ingresar: "))
            
            for i in range(N):
                num = int(input(f"Ingrese un número: "))
                lista_A.append(num)

            lista_B = nueva_lista_B(lista_A)
            print(f"Lista B: {lista_B}")

        except ValueError:
            print("No puede ser otro dato que no sea un número")

def ejercicio6():
    nueva_lista = []
    lista_N = []

    K = int(input("Ingrese un número entero: "))
    n = int(input("Ingrese la cantidad de números en la lista: "))

    for i in range(n):
        num = int(input(f"Ingrese un número para la lista N: "))
        lista_N.append(num)

        nueva_lista = insertar_K(lista_N, nueva_lista, K)

    print(f"Lista N: {lista_N}. Lista nueva: {nueva_lista}")

def ejercicio7():
    try:
        M = int(input("Ingrese el número de filas de la matriz: "))
        N = int(input("Ingrese el número de columnas de la matriz: "))
        
        matriz = []
        print("Ingrese los elementos de la matriz:")

        for i in range(M):
            fila = []

            for j in range(N):
                num = int(input(f"Elemento [{i+1},{j+1}]: "))
                fila.append(num)
            matriz.append(fila)
        
        print("Matriz:")
        mostrar_matriz(matriz)
        
        promedios_filas = promedio_fila(matriz)
        promedios_columnas = promedio_columna(matriz)
        
        print("Promedios de cada fila:", promedios_filas)
        print("Promedios de cada columna:", promedios_columnas)
        
    except ValueError:
        print("Ha ocurrido un error.")

def ejercicio8():
    try:
        M = int(input("Ingrese el tamaño de la matriz cuadrada (M): "))
        
        matriz = []
        print("Ingrese los elementos de la matriz:")

        for i in range(M):
            fila = []

            for j in range(M):
                num = int(input(f"Elemento [{i+1},{j+1}]: "))
                fila.append(num)
            matriz.append(fila)
        
        print("Matriz:")
        mostrar_matriz(matriz)
        
        suma_diag = suma_diagonal_principal(matriz)
        vector_resultante = filtrar_numeros(matriz, suma_diag)
        
        print("Suma de la diagonal principal:", suma_diag)
        print("Vector resultante sin repetidos:", vector_resultante)
        
    except ValueError:
        print("Ha ocurrido un error.")

def ejercicio9():
    try:
        M = int(input("Ingrese el número de filas de la matriz: "))
        N = int(input("Ingrese el número de columnas de la matriz: "))
        
        matriz = []
        print("Ingrese los elementos de la matriz:")
        for i in range(M):
            fila = []
            for j in range(N):
                num = int(input(f"Elemento [{i+1},{j+1}]: "))
                fila.append(num)
            matriz.append(fila)
        
        print("Matriz:")
        mostrar_matriz(matriz)
        
        k = int(input("Ingrese la fila k del elemento a verificar: "))
        h = int(input("Ingrese la columna h del elemento a verificar: "))
        
        if 0 <= k < M and 0 <= h < N:
            if es_punto_silla(matriz, k, h):
                print(f"El elemento A[{k},{h}] = {matriz[k][h]} es un punto silla.")
            else:
                print(f"El elemento A[{k},{h}] = {matriz[k][h]} NO es un punto silla.")
        else:
            print("Ha ocurrido un error.")
        
    except ValueError:
        print("Ha ocurrido un error.")

def ejercicio10():
    try:
        M = int(input("Ingrese el número de filas de la matriz: "))
        N = int(input("Ingrese el número de columnas de la matriz: "))
        
        matriz = []
        print("Ingrese los elementos de la matriz:")
        for i in range(M):
            fila = []
            for j in range(N):
                num = int(input(f"Elemento [{i+1},{j+1}]: "))
                fila.append(num)
            matriz.append(fila)
        
        print("Matriz:")
        mostrar_matriz(matriz)
        
        if es_simetrica(matriz):
            print("La matriz es simétrica.")
        else:
            print("La matriz NO es simétrica.")
        
    except ValueError:
        print("Ha ocurrido un error.")


def calculo_digitos_ent(num_entero):
    return len(str(abs(num_entero)))

def calculo_digitos_dec(num_decimal):
    num_a_texto = str(num_decimal)
    if "." in num_a_texto:
        decimales = num_a_texto.split(".")[1]

        return len(decimales)
    return 0

def cargar_compuestos(num,vector):
    div = 0
    copia = num

    for i in range(1,copia+1):
        if copia % i == 0:
            div += 1
    
    if div > 2:
        vector.append(num)

def invertir_con_auxiliar(vector):
    n = len(vector)
    v_auxiliar = [0] * n
    
    for i in range(n):
        v_auxiliar[i] = vector[n - 1 - i]
  
    for i in range(n):
        vector[i] = v_auxiliar[i]

    return vector
    
def invertir_sin_auxiliar(vector):
    i = 0
    j = len(vector) - 1
    while i < j:
        vector[i], vector[j] = vector[j], vector[i]
        i += 1
        j -= 1
    return vector

def elementos_B(N):
    parte_entera = abs(int(N))

    pares = 0
    impares = 0

    while parte_entera > 0:
        dig = parte_entera % 10

        if dig % 2 == 0:
            pares += 1
        else:
            impares += 1
        parte_entera //= 10

    return pares == 2 and impares >= 2

def nueva_lista_B(lista_A):
    return [num for num in lista_A if elementos_B(num)]

def imprimir_lista_B(lista_A, lista_B):
    print(f"Lista A: {lista_A}")
    print(f"Lista B: {lista_B}")

def insertar_K(lista_N, nueva_lista, K):
    nueva_lista = []
    for num in lista_N:
        nueva_lista.append(num)

        if num % K == 0:
             nueva_lista.append(K)
            
    return nueva_lista

import math

def promedio_fila(matriz):
    promedios = []
    for fila in matriz:
        suma = 0
        for num in fila:
            suma += num
        promedio = suma / len(fila)
        promedios.append(promedio)

    return promedios

def promedio_columna(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    promedios = []
    
    for j in range(columnas):
        suma = 0
        for i in range(filas):
            suma += matriz[i][j]
        promedio = suma / filas
        promedios.append(promedio)
    
    return promedios

def mostrar_matriz(matriz):
    for fila in matriz:
        for num in fila:
            print(num, end=" ")
        print()

def suma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

def filtrar_numeros(matriz, suma_diagonal):
    vector = []
    for fila in matriz:
        for num in fila:
            if math.factorial(num) >= suma_diagonal:
                vector.append(num)

    return list(set(vector))

def es_punto_silla(matriz, k, h):
    elemento = matriz[k][h]
    es_maximo_fila = elemento == max(matriz[k])
    es_minimo_columna = elemento == min(matriz[i][h] for i in range(len(matriz)))

    return es_maximo_fila and es_minimo_columna

def es_simetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas != columnas:
        return False
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

if __name__=="__main__":
    Menu()
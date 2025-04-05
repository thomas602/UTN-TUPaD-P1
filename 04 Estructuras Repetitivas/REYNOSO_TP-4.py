# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
def imprimir_numeros():
    for i in range(101):
        print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
def contar_digitos():
    numero = input("Ingrese un número entero: ")
    cantidad_digitos = len(numero)
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
def sumar_numeros():
    inicio = int(input("Ingrese el primer número: "))
    fin = int(input("Ingrese el segundo número: "))
    suma = 0
    for i in range(inicio + 1, fin):
        suma += i
    print(f"La suma de los números entre {inicio} y {fin} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0
def sumar_secuencial():
    suma = 0
    while True:
        numero = int(input("Ingrese un número entero (0 para salir): "))
        if numero == 0:
            break
        suma += numero
    print(f"La suma total es: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
def adivinar_numero():
    import random
    numero_aleatorio = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("Adivina el número entre 0 y 9: "))
        intentos += 1
        if intento == numero_aleatorio:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
        elif intento < numero_aleatorio:
            print("El número es mayor.")
        else:
            print("El número es menor.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
def imprimir_pares():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
def suma_hasta_numero():
    numero = int(input("Ingrese un número entero positivo: "))
    suma = 0
    for i in range(numero + 1):
        suma += i
    print(f"La suma de los números desde 0 hasta {numero} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
def contar_numeros():
    pares = 0
    impares = 0
    negativos = 0
    positivos = 0
    for i in range(100):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        if numero < 0:
            negativos += 1
        elif numero > 0:
            positivos += 1
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números negativos: {negativos}")
    print(f"Números positivos: {positivos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
def calcular_media():
    suma = 0
    for i in range(100):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        suma += numero
    media = suma / 100
    print(f"La media de los números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
def invertir_digitos():
    numero = input("Ingrese un número: ")
    numero_invertido = numero[::-1]
    print(f"El número invertido es: {numero_invertido}")

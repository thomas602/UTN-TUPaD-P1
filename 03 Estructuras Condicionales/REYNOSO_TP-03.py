# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 anos,
# deber mostrar un mensaje en pantalla que diga Es mayor de edad
def es_mayor_de_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deber
# mostrar por pantalla un mensaje que diga Aprobado; en caso contrario deber mostrar el
# mensaje Desaprobado
def aprobado_o_desaprobado():
    nota = float(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo nmeros pares. Si el usuario ingresa un
# nmero par, imprimir por en pantalla el mensaje "Ha ingresado un nmero par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un nmero par". Nota: investigar el uso del
# operador de mdulo (%) en Python para evaluar si un nmero es par o impar.
def numero_par():
    numero = int(input("Ingrese un numero par: "))
    if numero % 2 == 0:
        print("Ha ingresado un numero par")
    else:
        print("Por favor, ingrese un numero par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cul de las
# siguientes categoras pertenece:
# Nino/a: menor de 12 anos.
# Adolescente: mayor o igual que 12 anos y menor que 18 anos.
# Adulto/a joven: mayor o igual que 18 anos y menor que 30 anos.
# Adulto/a: mayor o igual que 30 anos.
def categoria_segun_edad():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Nino/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# 5) Escribir un programa que permita introducir contrasenas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contrasena de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contrasena correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contrasena de entre 8 y 14 caracteres". Nota: investigue el uso
# de la funcin len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
def contrasena_correcta():
    contrasena = input("Ingrese una contrasena de entre 8 y 14 caracteres: ")
    if 8 <= len(contrasena) <= 14:
        print("Ha ingresado una contrasena correcta")
    else:
        print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres")

# escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
import random


def sesgo():
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    if media < mediana < moda:
        print("Sesgo negativo")
    elif moda < mediana < media:
        print("Sesgo positivo")
    else:
        print("No hay sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, anadir un signo de exclamacin al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingres el usuario e imprimirlo por
# pantalla.
def agregar_signo():
    palabra = input("Ingrese una palabra: ")
    if palabra[-1] in "aeiou":
        print(palabra + "!")
    else:
        print(palabra)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el nmero 1, 2 o 3
# dependiendo de la opcin que desee:
# 1. Si quiere su nombre en maysculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opcin seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre maysculas y minsculas.
def transformar_nombre():
    nombre = input("Ingrese su nombre: ")
    opcion = int(
        input(
            "Ingrese 1 si quiere su nombre en mayusculas, 2 si quiere su nombre en minusculas o 3 si quiere su nombre con la primera letra mayuscula: "
        ))
    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    elif opcion == 3:
        print(nombre.title())
    else:
        print("Opcion invalida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categoras segn la escala de Richter e imprima el resultado
# por pantalla:
#  Menor que 3: "Muy leve" (imperceptible).
#  Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#  Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa danos).
#  Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar danos en estructuras
# dbiles).
#  Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar danos significativos).
#  Mayor o igual que 7: "Extremo" (puede causar graves danos a gran escala).
def magnitud_terremoto():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve")
    elif magnitud < 4:
        print("Leve")
    elif magnitud < 5:
        print("Moderado")
    elif magnitud < 6:
        print("Fuerte")
    elif magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")

# 10) Escribir un programa que pregunte al usuario en cul hemisferio se encuentra (N/S), qu mes
# del ano es y qué día es. El programa deber utilizar esa informacin para imprimir por pantalla
# si el usuario se encuentra en otono, invierno, primavera o verano.
from datetime import datetime

def estacion_del_ano():
    hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ")
    mes = int(input("Ingrese el mes del ano: "))
    dia = int(input("Ingrese el dia del mes: "))

    inicio_otonio = datetime.strptime("21/3/2025", "%d/%m/%Y")
    inicio_invierno = datetime.strptime("21/6/2025", "%d/%m/%Y")
    inicio_primavera = datetime.strptime("21/9/2025", "%d/%m/%Y")
    inicio_verano= datetime.strptime("21/12/2025", "%d/%m/%Y")

    fecha_usuario = datetime.strptime(f"{dia}/{mes}/2025", "%d/%m/%Y")

    if hemisferio == "S":
        if inicio_verano <= fecha_usuario:
            print("Verano")
        elif fecha_usuario <= inicio_invierno:
            print("Otono")
        elif fecha_usuario <= inicio_primavera:
            print("Invierno")
        else:
            print("Primavera")

    elif hemisferio == "N":
        if inicio_verano <= fecha_usuario:
            print("Invierno")
        elif fecha_usuario <= inicio_invierno:
            print("Primavera")
        elif fecha_usuario <= inicio_primavera:
            print("Verano")
        else:
            print("Otono")
    else:
        print("Hemisferio invalido")


estacion_del_ano()
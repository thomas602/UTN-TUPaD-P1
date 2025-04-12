# 1) Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
frutas = list(precios_frutas.keys())
# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
# mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
# años."
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(
            f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
# balanceados usando una pila.
def verificar_balance_parentesis(texto: str) -> bool:
    """
    Verifica si los paréntesis '()', '{}', '[]' en un string están
    correctamente balanceados usando una pila.

    Args:
        texto: El string que contiene los paréntesis a verificar.

    Returns:
        True si los paréntesis están balanceados, False en caso contrario.
    """
    pila = []
    mapa_parentesis = {")": "(", "}": "{", "]": "["}
    parentesis_apertura = set(mapa_parentesis.values()) # {'(', '{', '['}

    for caracter in texto:
        if caracter in parentesis_apertura:
            pila.append(caracter)
        elif caracter in mapa_parentesis:
            if not pila or pila[-1] != mapa_parentesis[caracter]:
                return False 
            pila.pop()

    return not pila 

# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:# Agregar clientes (encolar).
# Atender clientes (desencolar).
# Mostrar el siguiente cliente en la fila.
from collections import deque

class Banco:
    def __init__(self):
        self.cola_clientes = deque()

    def agregar_cliente(self, cliente):
        self.cola_clientes.append(cliente)

    def atender_cliente(self):
        if self.cola_clientes:
            return self.cola_clientes.popleft()
        else:
            return "No hay clientes en la fila."

    def siguiente_cliente(self):
        if self.cola_clientes:
            return self.cola_clientes[0]
        else:
            return "No hay clientes en la fila."
# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
# los valores almacenados.
class Nodo:
    """
    Representa un nodo individual en una lista simplemente enlazada.
    Cada nodo contiene datos y una referencia al siguiente nodo.
    """
    def __init__(self, dato):
        """
        Inicializa un nuevo nodo.

        Args:
            dato: El valor que se almacenará en el nodo.
        """
        self.dato = dato 
        self.siguiente = None 

class ListaEnlazada:
    """
    Representa una lista simplemente enlazada.
    Permite insertar nodos al inicio y recorrer la lista.
    """
    def __init__(self):
        """
        Inicializa una lista enlazada vacía.
        La cabeza (head) apunta a None inicialmente.
        """
        self.cabeza = None 

    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None

    def insertar_al_inicio(self, dato):
        """
        Inserta un nuevo nodo con el dato proporcionado al inicio de la lista.

        Args:
            dato: El valor para el nuevo nodo.
        """
        nuevo_nodo = Nodo(dato) 
        nuevo_nodo.siguiente = self.cabeza 
        self.cabeza = nuevo_nodo 
        print(f"Insertado al inicio: {dato}")

    def recorrer_y_mostrar(self):
        """
        Recorre la lista desde la cabeza hasta el final,
        mostrando el valor de cada nodo.
        """
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        print("Recorriendo la lista:")
        actual = self.cabeza 
        nodos_str = []
        while actual is not None:
            nodos_str.append(str(actual.dato)) 
            actual = actual.siguiente 

        print("Cabeza -> " + " -> ".join(nodos_str) + " -> None")    def invertir(self):
        """
        Invierte la lista enlazada modificando los punteros 'siguiente'.
        La cabeza original se convierte en la cola y la cola en la cabeza.
        """
        previo = None          
        actual = self.cabeza  
        siguiente_nodo = None  

        print("\n--- Iniciando inversión de la lista ---")
        print("Estado ANTES de invertir:")
        self.recorrer_y_mostrar()

        while actual is not None:
            siguiente_nodo = actual.siguiente

            actual.siguiente = previo

            previo = actual
            actual = siguiente_nodo

        self.cabeza = previo

        print("\nEstado DESPUÉS de invertir:")
        self.recorrer_y_mostrar()
        print("--- Inversión completada ---")#9) Dada una lista enlazada, implementa una función para invertirla.
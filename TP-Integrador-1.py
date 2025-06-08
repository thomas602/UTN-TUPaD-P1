from faker import Faker
import random
import timeit

class Student:
    """
    Clase que representa a un estudiante con nombre, apellido, DNI y nota.

    Args:
        first_name (str): Nombre del estudiante.
        last_name (str): Apellido del estudiante.
        dni (int): Documento Nacional de Identidad del estudiante.
        grade (float): Nota/calificación del estudiante.
    """
    def __init__(self, first_name, last_name, dni, grade):
        self.name = first_name
        self.last_name = last_name
        self.dni = dni
        self.grade = grade

    def __str__(self):
        """
        Devuelve una representación en string del estudiante.

        Returns:
            str: Cadena con apellido, nombre, DNI y nota del estudiante.
        """
        return f'{self.last_name} {self.name} {self.dni} {self.grade}'


def generate_students(students_amount):
    """
    Genera un listado de estudiantes con datos aleatorios.

    Args:
        students_amount (int): Cantidad de estudiantes a generar.

    Returns:
        list: Lista de objetos Student generados aleatoriamente.
    """
    faker = Faker()
    students = []
    for _ in range(students_amount):
        students.append(
            Student(
                faker.first_name(),
                faker.last_name(),
                random.randint(30000000, 50000000),
                round(random.uniform(1, 10), 2)
            )
        )
    return students

def bubble_sort(students):
    """
    Ordena una lista de estudiantes por su nota de mayor a menor usando el método de burbuja.

    Args:
        students (list): Lista de objetos Student a ordenar.

    Returns:
        list: Nueva lista de estudiantes ordenada por nota descendente.
    """
    sorted_students = students.copy()
    length = len(sorted_students)
    for i in range(length):
        for j in range(0, length - i - 1):
            if sorted_students[j].grade < sorted_students[j + 1].grade:
                sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
    return sorted_students

def selection_sort(students):
    """
    Ordena una lista de estudiantes según su nota usando el método de selección (de menor a mayor).

    Args:
        students (list): Lista de objetos Student a ordenar.

    Returns:
        list: Nueva lista de estudiantes ordenada por nota ascendente.
    """
    sorted_students = students.copy()
    length = len(sorted_students)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if sorted_students[j].grade < sorted_students[min_idx].grade:
                min_idx = j
        sorted_students[i], sorted_students[min_idx] = sorted_students[min_idx], sorted_students[i]
    return sorted_students

def lineal_search_by_dni(students, dni):
    """
    Busca un estudiante por su DNI utilizando búsqueda lineal.

    Args:
        students (list): Lista de objetos Student donde buscar.
        dni (int): DNI del estudiante a buscar.

    Returns:
        Student or None: El estudiante encontrado o None si no existe.
    """
    length = len(students)
    for i in range(length):
        if students[i].dni == dni:
            return students[i]
    return None

def binary_search_by_grade(students, target_grade):
    """
    Busca un estudiante por su nota utilizando búsqueda binaria.
    La lista de estudiantes debe estar ordenada por nota (preferentemente descendente).

    Args:
        students (list): Lista ordenada de objetos Student donde buscar.
        target_grade (float): Nota/calificación a buscar.

    Returns:
        Student or None: El estudiante encontrado o None si no existe.
    """
    left, right = 0, len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        if students[mid].grade == target_grade:
            return students[mid]
        elif students[mid].grade > target_grade:
            left = mid + 1
        else:
            right = mid - 1
    return None

# Programa Principal

# Genero el listado de estudiantes
students = generate_students(10000)

# Los ordeno usando el método de burbuja según la nota de cada uno
ordered_students = bubble_sort(students)

# Guardo los 1000 estudiantes con mejor calificación
filtered_students = ordered_students[:1000]

# Imprimo el nombre la calificación de los mejores 1000 estudiantes.
print("Nombre           DNI   Calificación")
for i, student in enumerate(filtered_students):
    print(student)

# Imprime por pantalla el tiempo que lleva ejecutar cada función
print("Tiempo que lleva ordenar los registros usando el método de burbuja: (en segundos)")
print(timeit.timeit(lambda: bubble_sort(students), number=1))
print("Tiempo que lleva ordenar los registros usando el método de selección: (en segundos)")
print(timeit.timeit(lambda: selection_sort(students), number=1))

# El usuario ingresa un DNI para buscar
dni = int(input("Ingrese DNI: "))
student_by_dni = lineal_search_by_dni(filtered_students, dni)
if student_by_dni:
    print(student_by_dni)
else:
    print("No se ha encontrado el registro")

#El usuario ingresa una nota para buscar
grade = float(input("Ingrese calificación: "))
student_by_grade = binary_search_by_grade(filtered_students, grade)
if student_by_grade:
    print(student_by_grade)
else:
    print("No se ha encontrado el registro")
from faker import Faker
import random
import timeit

class Student:
    def __init__(self, first_name, last_name, dni, grade):
        self.name = first_name
        self.last_name = last_name
        self.dni = dni
        self.grade = grade

    def __str__(self):
        return f'{self.last_name} {self.name} {self.dni} {self.grade}'


# Función que genera un listado de estudiantes, cada uno con su nombre y nota aleatorios.
def generate_students(students_amount):
    faker = Faker()
    students = []

    for _ in range(students_amount):
        students.append(Student(faker.first_name(), faker.last_name(), random.randint(30000000, 50000000), round(random.uniform(1, 10), 2)))

    return students

# Función que ordena los estudiantes según su nota usando el método de burbuja
def bubble_sort(students):
    sorted_students = students.copy()
    length = len(sorted_students)
    for i in range(length):
        for j in range(0, length - i - 1):
            if sorted_students[j].grade < sorted_students[j + 1].grade:
                sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
    return sorted_students

# Función que ordena los estudiantes según su nota usando el método de selección
def selection_sort(students):
    sorted_students = students.copy()
    length = len(sorted_students)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if sorted_students[j].grade < sorted_students[min_idx].grade:
                min_idx = j
        sorted_students[i], sorted_students[min_idx] = sorted_students[min_idx], sorted_students[i]
    return sorted_students

# Función que busca un estudiante por su DNI de manera LINEAL
def lineal_search_by_dni(students, dni):
    length = len(students)
    for i in range(length):
        if students[i].dni == dni:
            return students[i]
    return None

# Función que busca un estudiante por su nota de manera BINARIA
def binary_search_by_grade(students, target_grade):
    """
        Perform binary search on a sorted array.

        Args:
            students (list): A sorted list of elements.
            target_grade: The element to search for.

        Returns:
            int: The index of target in arr if present, else -1.
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




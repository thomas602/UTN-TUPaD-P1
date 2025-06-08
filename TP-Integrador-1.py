from faker import Faker
import random
import timeit

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


# Función que genera un listdado de estudiantes, cada con su nombre y nota aleatorios.
def generateStudents(studentsAmount):
    faker = Faker()
    students = []

    for _ in range(studentsAmount):
        students.append(Student(faker.name(), round(random.uniform(1, 10), 2)))

    return students

# Función que ordena los estudiantes según su nota usando el método de burbuja
def bubbleSort(students):
    sortedStudents = students.copy()
    length = len(sortedStudents)
    for i in range(length):
        for j in range(0, length - i - 1):
            if sortedStudents[j].grade < sortedStudents[j + 1].grade:
                sortedStudents[j], sortedStudents[j + 1] = sortedStudents[j + 1], sortedStudents[j]
    return sortedStudents

# Función que ordena los estudiantes según su nota usando el metodo de selección
def selection_sort(students):
    sortedStudents = students.copy()
    lenght = len(sortedStudents)
    for i in range(lenght):
        min_idx = i
        for j in range(i + 1, lenght):
            if sortedStudents[j].grade < sortedStudents[min_idx].grade:
                min_idx = j
        sortedStudents[i], sortedStudents[min_idx] = sortedStudents[min_idx], sortedStudents[i]
    return sortedStudents

students = generateStudents(10000)

#bubbleSort(students)
#selection_sort(students)

#for i, student in enumerate(students):
#   print(student.name, student.grade)


# Imprime por pantalla el tiempo que lleva ejecutar cada función
print(timeit.timeit(lambda: bubbleSort(students), number=1))
print(timeit.timeit(lambda: selection_sort(students), number=1))


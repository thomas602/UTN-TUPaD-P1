# TP-Integrador-1

Este proyecto es una simulación de gestión de estudiantes que permite generar datos aleatorios de estudiantes, ordenarlos por calificación usando distintos algoritmos, y realizar búsquedas por DNI y nota. Es ideal como práctica de programación en Python para materias iniciales de la Tecnicatura Universitaria en Programación a Distancia (UTN).

## Funcionalidades

- **Generación de estudiantes:** Crea una lista de estudiantes con nombre, apellido, DNI y calificación aleatorios usando la librería Faker.
- **Ordenamiento:** Implementa los algoritmos de ordenamiento Burbuja (Bubble Sort) y Selección (Selection Sort) para organizar los estudiantes según su calificación.
- **Búsquedas:** Permite buscar estudiantes por DNI (búsqueda lineal) o por calificación (búsqueda binaria).
- **Medición de tiempos:** Mide y muestra el tiempo que lleva ejecutar cada uno de los métodos de ordenamiento.
- **Interfaz por consola:** Permite ingresar un DNI y una calificación para buscar estudiantes en la lista de los mejores 1000.

## Requisitos

- Python 3.x
- [Faker](https://faker.readthedocs.io/) (`pip install Faker`)

## Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/thomas602/UTN-TUPaD-P1.git
   cd UTN-TUPaD-P1
   ```

2. Instala Faker si no lo tienes:
   ```bash
   pip install Faker
   ```

3. Ejecuta el script:
   ```bash
   python TP-Integrador-1.py
   ```

4. Sigue las instrucciones en pantalla para:
   - Ver los 1000 estudiantes con mejor calificación.
   - Buscar un estudiante por DNI.
   - Buscar un estudiante por calificación.

## Estructura del código

- **Clase Student:** Representa a un estudiante (nombre, apellido, DNI, nota).
- **generate_students:** Genera una lista de estudiantes con datos aleatorios.
- **bubble_sort y selection_sort:** Algoritmos de ordenamiento.
- **lineal_search_by_dni y binary_search_by_grade:** Algoritmos de búsqueda.
- **timeit:** Mide el tiempo de ejecución de los algoritmos de ordenamiento.

## Autor

- [thomas602](https://github.com/thomas602)

---

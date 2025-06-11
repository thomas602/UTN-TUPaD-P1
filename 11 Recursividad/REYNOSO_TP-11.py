def factorial(n):
    """Función recursiva que calcula el factorial de n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Función recursiva que calcula el número de Fibonacci en la posición n."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def potencia(base, exponente):
    """Función recursiva que calcula base elevado a exponente."""
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def decimal_a_binario(n):
    """Función recursiva que convierte un número decimal a binario como cadena."""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Prueba de la función
numero = int(input("Introduce un número entero positivo: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")

# Prueba de la función
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")


# Solicitar al usuario una posición
num = int(input("Introduce la posición hasta la que quieres mostrar la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {num}:")
for i in range(num + 1):
    print(f"F({i}) = {fibonacci(i)}")

# Solicitar al usuario un número entero positivo
num = int(input("Introduce un número entero positivo: "))

print(f"Factoriales del 1 al {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


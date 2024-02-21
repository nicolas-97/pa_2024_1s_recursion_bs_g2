def factorial(n):
    # Caso base: el factorial de 0 y 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial de (n - 1)
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    # Caso base: los primeros dos términos de la secuencia de Fibonacci son 0 y 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: la suma de los dos términos anteriores
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def sum_of_numbers(n):
    # Caso base: la suma de los primeros n números es 0 si n es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de los primeros (n - 1) números
    else:
        return n + sum_of_numbers(n - 1)

def power(a, n):
    # Caso base: cualquier número elevado a la potencia 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: a multiplicado por a elevado a la potencia (n - 1)
    else:
        return a * power(a, n - 1)

def max_in_list(lst):
    # Caso base: si la lista está vacía, no hay máximo
    if not lst:
        return None
    # Caso recursivo: el máximo entre el primer elemento y el máximo de la lista restante
    else:
        return max(lst[0], max_in_list(lst[1:]))

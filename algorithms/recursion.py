'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n * factorial(n - 1)
    return n * factorial(n - 1)

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        left_max = max_in_list(lst[:mid])
        right_max = max_in_list(lst[mid:])
        return max(left_max, right_max)

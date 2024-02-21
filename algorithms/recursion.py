'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    return n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    return n

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

'''
    Implementa una función recursiva para calcular a^n (a elevado a la power n).
'''

def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(a, -n)
    elif n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return a * power(a, n - 1)

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lst de enteros.
'''
def max_in_list(lst):
    if not lst:
        return None
    
    if len(lst) == 1:
        return lst[0]
    
    mitad = len(lst) // 2
    izquierda = max_in_list(lst[:mitad])
    derecha = max_in_list(lst[mitad:])
    
    if izquierda is None:
        return derecha
    elif derecha is None:
        return izquierda
    else:
        return max(izquierda, derecha)

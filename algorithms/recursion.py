"""
    Implementa una función recursiva para calcular el factorial de un número entero positivo
"""


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''


def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''


def sum_of_numbers(n):
    return n if n <= 0 else n + sum_of_numbers(n - 1)


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
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], max_in_list(lst[1:]))

'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        resultado = n * factorial(n-1)
    return resultado

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if n == 0:
       return 0
    elif n==1:
       return 1
    else:
        n = fibonacci(n-1)+fibonacci(n-2)
    return n

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_numbers(n-1)

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    if n == 0:
        return 1
    else:
        recuriva = power(a, n-1)
    return a * recuriva

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        inicio = lst[0]
        tail = lst[1:]
        final = max_in_list(tail)
        if inicio > final:
            return inicio
        else:
            return final
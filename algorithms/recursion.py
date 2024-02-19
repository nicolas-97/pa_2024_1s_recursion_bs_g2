'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    return n

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >= 3:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return n + sum_of_numbers(n - 1)
    return n 


'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    if a == 1 or n == 0:
        return 1
    elif n == 1:
        return a
    elif a > 1 and n > 1:
        return a * power(a, n - 1)
    return a + n

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    if lst == []:
        return None
    else:
        return max_in_list_dos(lst, lst[0])
    

def max_in_list_dos(lst, max):
    if lst == []:
        return max
    
    if lst[0] > max:
        max = lst[0]
    
    return max_in_list_dos(lst[1:], max)

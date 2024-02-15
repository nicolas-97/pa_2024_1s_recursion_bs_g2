'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
from random import sample 
lista = list(range(100))


def factorial(n):
    n = int(input())
    for i in (n):
        n * factorial(n-1)
        print("El factorial del número es: ",factorial) 
    else:
        print("[ERROR]: El algoritmo es solo para obtener el factorial de números mayores a cero")
    return factorial

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    a = int(input())
    b = int(input())
    sum = 0
    pot = 0
    for i in (a < b):
        pot = 2**(a+1)
        sum += pot
    print("El término que busca es: ",fibonacci)
    return fibonacci

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''

arr = sample(lista,10) 

def sum_of_numbers(lista):
    a = 0
    b = 1
    sum_of_numbers = sum(a + b)
    return sum_of_numbers

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    a = int(input())
    n = int(input())
    exp = a**n
    return power

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    arr = sample(lista,10)
    max = len(lista)
    min = 0
    for max in lista:
        if max > min:
            max == max
        else:
            min, max == max, min
    return max_in_list
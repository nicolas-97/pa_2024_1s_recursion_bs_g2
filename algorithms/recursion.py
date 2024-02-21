'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1) 
    
print(factorial(8))


'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):

    if n <2:
        return n
    return fibonacci(n-1)+ fibonacci(n-2)
for x in range (15):
    print (fibonacci(x))

    

'''Implementa una función recursiva para calcular la suma de los primeros n números enteros.'''
def sum_of_numbers(x):
    if x ==0:
        return x
    else:
        return x + sum_of_numbers(x-1)

resultado=sum_of_numbers(5)
print(resultado)



    return n

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    
    return n 


'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):

    if n == 0:
        return 1
    else:
        return a * power(a,n-1)
resultado = power(2,5)
print(resultado)


    
    return a + n


'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):

    if len(lst) == 1:
        return lst[0]
    else:
        maximo_resto = max_in_list(lst[1:])  # Corregir el índice
        return maximo_resto if maximo_resto > lst[0] else lst[0]

numeros = [4, 8, 2, 10, 5]
maximo = max_in_list(numeros)
print(maximo)

    
    return lst


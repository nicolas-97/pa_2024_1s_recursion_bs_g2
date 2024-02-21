def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def max_in_list(lst):
    if not lst:
        return None 
    elif len(lst) == 1:
        return lst[0]
    else:
        max_rest = max_in_list(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest


def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)




        

    



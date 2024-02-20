def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)   

def fibonacci(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    

def sum_of_numbers(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n+sum_of_numbers(n-1)  

def power(a, n):
    if n==0:
        return 1
    if n==1:
        return a
    else:
        return a*power(a,n-1)

def max_in_list(lst):
    listaa=lst[:]

    if len(listaa)==1:
        return listaa[0]
    else:
        if listaa[0]>listaa[1]:
            listaa.pop(1)
            return max_in_list(listaa)
        if listaa[1]>listaa[0]:
            listaa.pop(0)
            return max_in_list(listaa)
        if listaa[1]==listaa[0]:
            listaa.pop(0)
            return max_in_list(listaa)

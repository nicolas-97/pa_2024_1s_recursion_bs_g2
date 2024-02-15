from models.tree_node import TreeNode
from random import sample 
lista = list(range(100))
arr = sample(lista,10) 

def binary_search(arr: list, target: int):
    i = 4
    left = 0
    right = len(arr) -1
    target = (left + right) // 2
    while right > left:
        if target > i & i > left:
             left = target + 1
             right = len(arr) -1
             target = (left + right) // 2
        elif target < right:
            right = target - 1
            left = target + 1
            target = (left + right) // 2 
            print(binary_search,i,target)
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si encuentra el elemento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    i = 4
    left = 0
    right = matrix.shape -1
    target = (left + right) // 2
    while left <= right:
        if target != i & i > left:
             left = target + 1
             right = matrix.shape -1
             target = (left + right) // 2
        else:
            right = target + 1
            left = target - 1
            target = (left + right) // 2 

    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si encuentra el elemento o falso si no lo encuentra
'''
def binary_search_tree(root: tree_node, target: int):
    
    return False
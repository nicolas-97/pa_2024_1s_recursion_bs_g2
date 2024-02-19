from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    minimo=0
    maximo= len(arr) -1

    return binary_recursive(arr, minimo, maximo, target)
    
def binary_recursive(arr: list, minimo, maximo, target: int):
    if len(arr) == 0:
        return -1
    elif maximo >= minimo:
        medio = (minimo + maximo) // 2
        if arr[medio] == target:
            return medio
        elif arr[medio] > target:
            return binary_search(arr, minimo, medio -1, target)
        else:
            return binary_search(arr, medio +1, maximo, target)
    else:
        return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    return False

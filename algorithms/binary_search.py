from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr, menor, mayor, buscado):
     
    if mayor >= menor:
 
        mid = (mayor + menor) // 2
 
        if arr[mid] == buscado:
            return mid
        elif arr[mid] > buscado:
            return binary_search(arr, menor, mid - 1, buscado)
        else:
            return binary_search(arr, mid + 1, mayor, buscado)
 
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

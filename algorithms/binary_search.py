from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr, numero):
    menor = 0
    alto = len(arr) - 1
    med = 0
 
    while menor <= alto:
 
        med = (alto + menor) // 2
 
        # If numero is greater, ignore left half
        if arr[med] < numero:
            menor = med + 1
 
        # If numero is smaller, ignore right half
        elif arr[med] > numero:
            alto = med - 1
 
        # means numero is present at med
        else:
            return med
 
    # If we reach here, then the element was not present
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

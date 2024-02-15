from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, meta: int) -> int:
    izq, der = 0, len(arr) - 1
    
    while izq <= der:
        mitad = izq + (der - izq) // 2
        if arr[mitad] == meta:
            return mitad
        elif arr[mitad] < meta:
            izq = mitad + 1
        else:
            der = mitad - 1
    
    return -1


'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], meta: int) -> bool:
    if not matrix:
        return False
    
    filas, colms = len(matrix), len(matrix[0])
    fila, colum = 0, colms - 1
    
    while fila < filas and colum >= 0:
        if matrix[fila][colum] == meta:
            return True
        elif matrix[fila][colum] < meta:
            fila += 1
        else:
            colum -= 1
    
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(inicio: TreeNode, meta: int) -> bool:
    if not inicio:
        return False
    
    actual = inicio
    while actual:
        if actual.val == meta:
            return True
        elif actual.val < meta:
            actual = actual.right
        else:
            actual = actual.left
    
    return False
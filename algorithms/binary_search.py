from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int) -> int:
    inicial = 0
    final = len(arr) - 1
    while inicial <= final:
        medio = (inicial + final) // 2
        if arr[medio] == target:
            return medio
        elif arr[medio] < target:
            inicial = medio + 1
        else:
            final = medio - 1
    return -1


'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    
    filas, columnas = len(matrix), len(matrix)
    fila_matriz, columna_matriz = 0, columnas - 1 

    while fila_matriz < filas and columna_matriz >= 0:
        if matrix[fila_matriz][columna_matriz] == target:
            return True
        elif matrix[fila_matriz][columna_matriz] < target:
            fila_matriz = fila_matriz + 1  
        else:
            columna_matriz = columna_matriz- 1 
    return False


'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False
    
    if root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)
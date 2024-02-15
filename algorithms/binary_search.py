from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
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
    if not matrix or not matrix[0]:
        return False
    
    filas = len(matrix)
    columnas = len(matrix[0])
    
    izq, dere = 0, filas * columnas - 1
    
    while izq <= dere:
        medio = (izq + dere) // 2
        elemento_medio = matrix[medio // columnas][medio % columnas]
        
        if elemento_medio == target:
            return True
        elif elemento_medio < target:
            izq = medio + 1
        else:
            dere = medio - 1
    
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

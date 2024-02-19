from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    def bynary_search_recursive(arr, target, low, high):
        if low <= high:
            mid= (low + high)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return bynary_search_recursive(arr , target, mid + 1, high)
            else:
                return bynary_search_recursive(arr, target, low, mid - 1)
        else:
            return -1
    return bynary_search_recursive(arr, target, 0, len(arr)-1)

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    filas= len(matrix)
    columnas = len(matrix[0])

    inicio = 0
    fin = filas * columnas - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        fila = medio // columnas
        columna = medio % columnas
        
        if matrix[fila][columna] == target:
            return True
        elif matrix[fila][columna] < target:
            inicio = medio + 1
        else:
            fin = medio - 1

    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def binary_search_tree(root: TreeNode, target: int) ->bool:
    if not root:
        return False
    if root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)
    

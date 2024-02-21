from ..models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''

# arr = [1,2,3]
# target = 0
def binary_search(arr: list, target: int):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Elemento encontrado, retornamos su posición
        elif arr[mid] < target:
            left = mid + 1  # Búsqueda en la mitad derecha
        else:
            right = mid - 1  # Búsqueda en la mitad izquierda

    return -1  # Elemento no se encuentra en la lista

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    if not matrix:
        return False

    nrows = len(matrix)
    ncols = len(matrix[0])

    left = 0
    right = nrows * ncols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // ncols][mid % ncols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root is None or root.val == target:
        return root is not None

    # El valor del nodo actual es mayor entonces ir al subárbol izquierdo
    if root.val > target:
        return binary_search_tree(root.left, target)

    # O ir al subárbol derecho
    return binary_search_tree(root.right, target)

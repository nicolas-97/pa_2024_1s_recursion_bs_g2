from models.tree_node import TreeNode
'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posición si no lo encuentra que retorne -1
'''
def binary_search(arr: list, target: int):
    def search(arr, target, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return search(arr, target, mid + 1, end)
        else:
            return search(arr, target, start, mid - 1)

    return search(arr, target, 0, len(arr) - 1)

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuentra el elemento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    def search(matrix, target, row, col):
        if row >= len(matrix) or col < 0:
            return False
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            return search(matrix, target, row + 1, col)
        else:
            return search(matrix, target, row, col - 1)

    if not matrix or not matrix[0]:
        return False
    return search(matrix, target, 0, len(matrix[0]) - 1)

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuentra el elemento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if not root:
        return False
    if root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)

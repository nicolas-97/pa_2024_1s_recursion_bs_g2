from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    inicio=0
    fin=(len)-1
    while inicio <= fin:
        mitad=(inicio+fin)/2
        if [mitad]== int:
            return mitad
        elif [mitad] < int:
            inicio = mitad+1
        else:
            fin= mitad-1
             
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    if not matrix or not matrix[0]:
        return False  # Empty matrix

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

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
    if not root:
        return False  # Empty tree

    while root:
        if root.val == target:
            return True
        elif root.val < target:
            root = root.right
        else:
            root = root.left

    return False

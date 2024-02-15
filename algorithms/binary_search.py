from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posición si no lo encuentra que retorne -1
'''
def binary_search(arr: list, target: int):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuentra el elemento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    if not matrix:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
            
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda y retorne verdadero si la encuentra el elemento o falso si no lo encuentra
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

from models.tree_node import TreeNode

def binary_search(arr: list, target: int):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Elemento encontrado, retorna la posición
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Elemento no encontrado en la lista

def binary_search_matrix(matrix: list[list[int]], target: int):
    rows, cols = len(matrix), len(matrix[0]) if matrix and matrix[0] else 0
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True  # Elemento encontrado en la matriz
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False  # Elemento no encontrado en la matriz


def binary_search_tree(root: TreeNode, target: int):
    if not root:
        return False  # Árbol vacío, elemento no encontrado
    elif root.val == target:
        return True  # Elemento encontrado en el árbol
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)
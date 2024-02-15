from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    left= 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] ==  target:
            return mid
        elif arr[mid] < target:
            left=mid+1
        else:
            right = mid -1    
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    rows, cols = len(matrix), len(matrix)
    low, high=0, rows * cols -1

    while low <= high:
        mid=(low+high)//2
        row, col = divmod(mid,cols)
        mid_val = matrix[row][col]
        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid +1
        else:
            high = mid - 1
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False
    
    if root.val==target:
        return True
    elif root.val<target:
        return binary_search_tree(root.right,target)
    else:
        return binary_search_tree(root.left,target)
    return False

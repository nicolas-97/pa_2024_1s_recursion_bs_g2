from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):

    left = 0
    rigth = -1
    middle = (left + rigth)//2
    while middle > 3:
        if arr[middle]==target:
            return middle
        elif arr[middle]>target:
            rigth = middle-1
            return binary_search(arr)
        elif arr[middle]>target:
            left = middle+1
            return binary_search(arr)
    if target == arr[middle]:
        return middle
    elif target > arr[middle]:
        return (middle+1)
    elif target < arr[middle]:
        return (middle-1)
    else:
        return -1
'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    return False

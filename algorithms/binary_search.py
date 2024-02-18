from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int,left = 0 ,rigth = 0):

    if left+rigth == 0:
        rigth = len(arr)

    if rigth<=left:
        middle = (left + rigth)//2
        if arr[middle]==target:
            return middle
        elif arr[middle] > target:
            return binary_search(arr,target, left, middle-1)
        elif arr[middle] < target:
            return binary_search(arr,target, middle+1, rigth)
        else:
            return -1
    else:
        return -1
    
'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    for i in range(len(matrix)):
        if binary_search(matrix[i],target) == -1:
            return False
        else:
            return True        

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    return False

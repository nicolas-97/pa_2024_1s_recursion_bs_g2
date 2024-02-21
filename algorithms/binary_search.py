from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = arr[medio]

        if valor_medio == target:
            return medio
        elif valor_medio < target:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1
'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    for fila in matrix:
        inicio = 0
        fin = len(fila) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            valor_apuntado = fila[medio]

            if valor_apuntado == target:
                return True
            elif valor_apuntado < target:
                inicio = medio + 1
            else:
                fin = medio - 1
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    
    return False
    

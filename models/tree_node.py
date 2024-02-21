class TreeNode:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None

def busqueda_binaria_arbol(root: TreeNode, objetivo: int):
    # Caso base: si el nodo actual es None, no se encontró el elemento
    if root is None:
        return False

    # Comparar el valor del nodo actual con el objetivo
    if root.val == objetivo:
        return True  # Elemento encontrado

    # Si el objetivo es menor, buscar en el subárbol izquierdo
    elif objetivo < root.val:
        return busqueda_binaria_arbol(root.left, objetivo)

    # Si el objetivo es mayor, buscar en el subárbol derecho
    else:
        return busqueda_binaria_arbol(root.right, objetivo)

# Crear un árbol de búsqueda binaria
#       5
#      / \
#     3   8
#    / \ / \
#   2  4 6  9
raiz = TreeNode(5)
raiz.left = TreeNode(3)
raiz.right = TreeNode(8)
raiz.left.left = TreeNode(2)
raiz.left.right = TreeNode(4)
raiz.right.left = TreeNode(6)
raiz.right.right = TreeNode(9)

elemento_objetivo = 9
resultado = busqueda_binaria_arbol(raiz, elemento_objetivo)

# Verificación del resultado y presentación en consola
if resultado:
    print(f"¡Encontrado! El elemento {elemento_objetivo} está en el árbol.")
else:
    print(f"No encontrado. El elemento {elemento_objetivo} no está en el árbol.")
from models.tree_node import TreeNode

def binary_search(arr: list, target: int):
    izq=0
    der=len(arr)-1

    while izq<=der:
        medio=(izq+der)//2

        if arr[medio]==target:
            return medio
        elif arr[medio]<target:
            izq=medio+1
        else:
            der=medio-1
    return -1
    
def binary_search_matrix(matrix: list[list[int]], target: int):
    if not matrix: return False
    n=len(matrix[0])
    m=len(matrix)
    izq,der=0,(n*m)-1

    while izq<=der:
        medio=(izq+der)//2
        if matrix[medio//n][medio%n]==target:
            return True
        elif matrix[medio//n][medio%n]<target:
            izq=medio+1
        else:
            der=medio-1
   
    return False

def binary_search_tree(root: TreeNode, target: int):
        if root.val==target:
            return True
        if target<root.val:
            if root.left:
                binary_search_tree(root.left,target)
            else:
                return False
        if target>root.val:
            if root.right:
                binary_search_tree(root.right,target)
            else:
                return False
    
    

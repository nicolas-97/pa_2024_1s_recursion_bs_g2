from models.tree_node import TreeNode

def binary_search(arr: list, target: int):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        
        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_matrix(matrix: list[list[int]], target: int):
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    
    while row < rows and col >= 0:
        current_value = matrix[row][col]
        if current_value == target:
            return True
        elif current_value < target:
            row += 1
        else:
            col -= 1
    
    return False

def binary_search_tree(root: TreeNode, target: int):
    if not root:
        return False
    
    if root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)


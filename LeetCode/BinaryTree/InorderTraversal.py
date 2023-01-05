# Given the root of a binary tree, return the 
# inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def inorderTraversal(root):
    traversal = []
    if(not root):
        return 

    if(root.left):
        traversal += inorderTraversal(root.left)

    traversal.append(root.val)
        
    if(root.right):
        traversal += inorderTraversal(root.right)
    return traversal 

if __name__ == "__main__":
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    print(inorderTraversal(root))



# Given the root of a binary tree, return its 
# maximum depth.
# A binary tree's maximum depth is the number
#  of nodes along the longest path from the root 
#  node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(self, root):
    height = 1
    countL = 0
    countR = 0 

    if(not root):
        return 0

    if(root.left):
        countL = height + self.maxDepth(root.left)

    if(root.right):
        countR = height + self.maxDepth(root.right)

    if(countL > countR):
        return countL
    else:
        return countR 
    
# Given the root of an n-ary tree, return the preorder traversal of
#  its nodes' values.Nary-Tree input serialization is represented 
#  in their level order traversal. Each group of children is 
#  separated by the null value 

def __init__(self):
    self.stack = []

def preorder(self, root: 'Node') -> List[int]:
    if(not root):
        return self.stack
    self.stack.append(root.val)
    if (root.children):
        for i in root.children:
            self.preorder(i)
    return self.stack

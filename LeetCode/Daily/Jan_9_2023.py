# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(root,l):
    if root==None:
        return l

    l.append(root.val)
    l = traverse(root.left,l)
    l = traverse(root.right, l)
    return l    

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return traverse(root,[])

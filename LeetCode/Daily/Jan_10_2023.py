# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(root,l):
    if root==None:
        l.append('null')
        return l
    l.append(root.val)
    l = traverse(root.left,l)
    l = traverse(root.right,l)
    return l
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if traverse(p,[])==traverse(q,[]):
            return True
        return False

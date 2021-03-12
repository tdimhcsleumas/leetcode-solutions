# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []
        
        while root:
            print(stack)
            
            if root.left:
                temp = root.left
                root.left = None
                stack.append(root)
                root = temp
                continue
           
            output.append(root.val)
            
            if root.right:
                root = root.right
                continue
                
            if stack:
                root = stack.pop()
            else:
                break
            
        return output

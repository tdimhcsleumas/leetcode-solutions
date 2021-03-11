class Solution:
    def _deepestLeavesSum(self, root: TreeNode, depth):
        if not root.left and not root.right:
            return (depth, root.val)
        if root.left and root.right:
            left = self._deepestLeavesSum(root.left, depth+1)
            right = self._deepestLeavesSum(root.right, depth+1)
            if left[0] == right[0]:
                return (left[0], left[1] + right[1])
            elif left[0] > right[0]:
                return left
            else:
                return right
        if root.left:
            return self._deepestLeavesSum(root.left, depth+1)
        if root.right:
            return self._deepestLeavesSum(root.right, depth+1)            
                
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self._deepestLeavesSum(root, 0)[1]

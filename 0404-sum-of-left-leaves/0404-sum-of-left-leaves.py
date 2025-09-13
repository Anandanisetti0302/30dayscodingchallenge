class Solution(object):
    def sumOfLeftLeaves(self, root):
        def is_leaf(node):
            return node and not node.left and not node.right
        def dfs(node):
            if not node:
                return 0
            total = 0
            if is_leaf(node.left):
                total += node.left.val
            total += dfs(node.left)
            total += dfs(node.right)
            return total
        return dfs(root)

        
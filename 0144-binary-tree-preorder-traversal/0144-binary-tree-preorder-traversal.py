class Solution(object):
    def preorderTraversal(self, root):
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res

        
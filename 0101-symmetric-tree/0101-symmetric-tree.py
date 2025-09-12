class Solution(object):
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(root.left, root.right)

        
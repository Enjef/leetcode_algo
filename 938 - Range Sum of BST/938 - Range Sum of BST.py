class Solution:
    def rangeSumBST_my(self, root, low, high):  # 34%
        if not root:
            return 0
        current = root.val
        if not(low <= current <= high):
            current = 0
        if not root.left and not root.right:
            return current
        return (
            current +
            self.rangeSumBST_my(root.left, low, high) +
            self.rangeSumBST_my(root.right, low, high)
        )

    def rangeSumBST_best(self, root: TreeNode, low: int, high: int) -> int:
        if (not root):
            return 0
        if (root.val < low):
            return self.rangeSumBST_best(root.right, low, high)
        if (root.val > high):
            return self.rangeSumBST_best(root.left, low, high)
        return (
            root.val +
            self.rangeSumBST_best(root.left, low, high) +
            self.rangeSumBST_best(root.right, low, high)
        )

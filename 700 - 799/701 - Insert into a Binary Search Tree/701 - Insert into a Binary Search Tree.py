# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:  # 64% 54%
        if not root:
            return TreeNode(val)
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        if val >= root.val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        return root

    def insertIntoBST_stack(self, root: TreeNode, val: int) -> TreeNode:
        stack = [root]  # 83.93% 24.62%
        while stack:
            cur = stack.pop()
            if not cur:
                return TreeNode(val)
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                else:
                    stack.append(cur.left)
            if val >= cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                else:
                    stack.append(cur.right)
        return root

    def insertIntoBST_best_speed(
            self,
            root: Optional[TreeNode],
            val: int) -> Optional[TreeNode]:
        def dfs(root, val):
            if root is None:
                return TreeNode(val)
            if root.val < val:
                root.right = dfs(root.right, val)
            elif root.val > val:
                root.left = dfs(root.left, val)
            return root
        return dfs(root, val)

    def insertIntoBST_best_memory(
            self,
            root: Optional[TreeNode],
            val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root

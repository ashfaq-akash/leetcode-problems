# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def insertIntoBST(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = TreeNode.insertIntoBST(root.left, val)
        else:
            root.right = TreeNode.insertIntoBST(root.right, val)
        return root

    @staticmethod
    def listToBST(nums):
        root = None
        for num in nums:
            root = TreeNode.insertIntoBST(root, num)
        return root

class Solution:
    def searchBST(self, root, val: int):
        if not root:
            return None
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root

sol = Solution()
root = TreeNode.listToBST([4,2,7,1,3])
print(sol.searchBST(root, 2))

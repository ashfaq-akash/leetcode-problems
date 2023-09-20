from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) :
        if not root:
            return TreeNode(val)
        
        if val>root.val:
            root.right=self.insertIntoBST(root.right,val)
        elif val<root.val:
            root.left=self.insertIntoBST(root.left,val)
        
        return root
    
    def listToBST(self,nums):
        if not nums:
            return None
        
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.listToBST(nums[:mid])
        root.right=self.listToBST(nums[mid+1:])

        return root


sol=Solution()
root = sol.listToBST([10, 20, 30, 40, 50, 60, 70])
print(sol.insertIntoBST(root,25))

#APPROACH 1: O(N)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            lh=height(root.left)
            rh=height(root.right)
            if lh==-1 or rh==-1:
                return -1
            if abs(lh-rh)>1:
                return -1
            return 1+max(lh,rh)
        return height(root) != -1



#Approach 2:O(N*N)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            lh=height(root.left)
            rh=height(root.right)
            return 1+max(lh,rh)


        if not root:
            return True
        lh=height(root.left)
        rh=height(root.right)  
        if abs(lh-rh)>1:
            return False
        left=self.isBalanced(root.left)
        right=self.isBalanced(root.right)
        if not left or not right:
            return False
        return True

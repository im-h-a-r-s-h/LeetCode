# LeetCode Problem: 1261. Find Elements in a Contaminated Binary Tree
# Problem Link: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        temp = root
        root.val = 0
        self.d = set()
        
        def dfs(temp):
            if temp is None:
                return
            self.d.add(temp.val)
            if temp.left:
                temp.left.val = (temp.val * 2) + 1
                dfs(temp.left)
            if temp.right:
                temp.right.val = (temp.val * 2) + 2
                dfs(temp.right)
        
        dfs(temp)

    def find(self, target: int) -> bool:
        return target in self.d

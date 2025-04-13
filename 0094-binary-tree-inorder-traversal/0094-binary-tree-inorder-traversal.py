# LeetCode Problem: 94. Binary Tree Inorder Traversal
# Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal
 
#Approach 1: Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        stack=[]
        node=root
        while(stack or node):
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                ans.append(node.val)
                node=node.right  
        return ans
Approach 2: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorderf(node,ans):
            if not node:
                return []

            inorderf(node.left,ans)
            ans.append(node.val)
            inorderf(node.right,ans)
            return ans
        return inorderf(root,[])
Approach 3: All 3 traversals in one Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversals(node):
            pre,post,inorder=[],[],[]
            stack=[(root,1)]
            while(stack):
                node,state=stack.pop()
                if state==1:
                    pre.append(node.val)
                    stack.append((node,2))
                    if node.left:
                        stack.append((node.left,1))
                elif state==2:
                    inorder.append(node.val)
                    stack.append((node,3))
                    if node.right:
                        stack.append((node.right,1))
                elif state==3:
                    post.append(node.val)
            return inorder
        if not root:
            return []     
        return traversals(root)

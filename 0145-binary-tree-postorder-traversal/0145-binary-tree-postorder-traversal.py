# LeetCode Problem: 145. Binary Tree Postorder Traversal
# Problem Link: https://leetcode.com/problems/binary-tree-postorder-traversal

Approach 1: Iterative (1 stack)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                temp=stack[-1].right
                if not temp:
                    temp=stack.pop()
                    ans.append(temp.val)
                    while(stack and temp==stack[-1].right):
                        temp=stack.pop()
                        ans.append(temp.val)
                else:
                    node=temp
        return ans
        
Approach 2: Iterative (2 stack)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack1=[]
        stack2=[]
        stack1.append(root)
        while(stack1):
            node=stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node.val)
        return stack2[::-1]
        
Approach 3: Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node,ans):
            if not node:
                return []

            postorder(node.left,ans)
            postorder(node.right,ans)
            ans.append(node.val)
            return ans
        return postorder(root,[])


Approach 4: All 3 traversals in one Iteration
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
            return post
        if not root:
            return []     
        return traversals(root)

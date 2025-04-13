# LeetCode Problem: 102. Binary Tree Level Order Traversal
# Problem Link: https://leetcode.com/problems/binary-tree-level-order-traversal

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
            return pre
        if not root:
            return []     
        return traversals(root)

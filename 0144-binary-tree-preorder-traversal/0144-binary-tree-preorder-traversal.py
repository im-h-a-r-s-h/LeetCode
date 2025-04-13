# LeetCode Problem: 144. Binary Tree Preorder Traversal
# Problem Link: https://leetcode.com/problems/binary-tree-preorder-traversal

#Approach 1: Iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        stack=[]
        stack.append(root)
        while(stack):
            node=stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            ans.append(node.val)
        return ans


#Approach 2: Recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def pre(node,ans):
            if not node:
                return []
            ans.append(node.val)
            pre(node.left,ans)
            pre(node.right,ans)
            return ans
        return pre(root,[])


#Approach 3: All 3 traversals in one Iteration
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

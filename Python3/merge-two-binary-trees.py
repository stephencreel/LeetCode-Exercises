# https://leetcode.com/problems/merge-two-binary-trees/
#
# Program merges two binary trees given tree's root as input.
#
# Runtime: 76 ms, faster than 99.54% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 13.7 MB, less than 82.39% of Python3 online submissions for Merge Two Binary Trees.
# (6/2/2019)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if not t1:
            root = t2
        elif not t2:
            root = t1
        else:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        return root

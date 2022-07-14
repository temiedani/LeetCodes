
# LeetCode 226. Invert Binary Tree
'''
Given the root of a binary tree, 
invert the tree, and return its root.
'''
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        current_node = root
        if not root:
            return None

        current_node.left, current_node.right = current_node.right, current_node.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return current_node


if __name__ == "__main__":
    # Input:
    root = [4, 2, 7, 1, 3, 6, 9]
    # Output:
    # [4,7,2,9,6,3,1]
    # test = Solution()
    # print(test.invertTree(root))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def deleteNode(self, key):
        # check if empty root
        if not self.val:
            return None
        # check base node
        elif key == self.val:
            pass
        # check left node
        elif key < self.val:
            self.left.deleteNode(key)

        # check righ node
        elif key > self.val:
            self.right.deleteNode(key)

        return self.root


if __name__ == '__main__':
    print("result")
    my_tree = TreeNode(12, 5, 14)
    my_tree.deleteNode(5)

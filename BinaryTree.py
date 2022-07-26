
from datetime import date


class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # if node already exist
        if(self.data == data):
            return
        elif data < self.data:
            # if left nodeis empty
            if self.left == None:
                self.left = BinarySearchTreeNode(data)
            else:
                # recursive call
                self.left.add_child(data)
        elif data > self.data:
            # if right nodeis empty
            if self.right == None:
                # create a new node
                self.right = BinarySearchTreeNode(data)
            else:
                # recursive call
                self.right.add_child(data)

    def in_order_traversal(self):
        result = []
        # left tree
        if self.left:
            result += self.left.in_order_traversal()
        # base node
        result.append(self.data)

        # left tree
        if self.right:
            result += self.right.in_order_traversal()
        return result

    def pre_order_traversal(self):
        result = []
        # base node
        result.append(self.data)
        # left tree
        if self.left:
            result += self.left.pre_order_traversal()

        # left tree
        if self.right:
            result += self.right.pre_order_traversal()
        return result

    def post_order_traversal(self):
        result = []
        # left tree
        if self.left:
            result += self.left.post_order_traversal()
        # left tree
        if self.right:
            result += self.right.post_order_traversal()
        # base node
        result.append(self.data)
        return result

    def Search(self, val):
        if val == self.data:
            return True
        #  check left tree
        elif val < self.data:
            if self.left:
                return self.left.Search(val)
            else:
                return False
        #  check right tree
        elif val > self.data:
            if self.right:
                return self.right.Search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            min = self.left.find_min()
        else:
            min = self.data
        return min

    def find_max(self):
        if self.right:
            max = self.right.find_max()
        else:
            max = self.data
        return max

    def calculate_sum(self) -> int:
        sum = 0
        # add the base node
        sum += self.data
        # add the left node
        if self.left:
            sum += self.left.calculate_sum()
        # add the right node
        if self.right:
            sum += self.right.calculate_sum()
        return sum

    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            # no child
            if self.left is None and self.right is None:
                return None
            #  one right child
            elif self.left is None:
                return self.right
            #  one left
            elif self.right is None:
                return self.left
            # two child
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
            # or equavalently we could do
            # max_val=self.left.find_max()
            # self.data=max_val
            # self.left=self.left.delete_node(max_val)
        return self


def build_tree(element):
    root = BinarySearchTreeNode(element[0])
    for i in element[1:]:
        root.add_child(i)
    return root


if __name__ == "__main__":
    # numbers = [5, 4, 3, 2, 1, 6, 7, 8, 9, 5, -1, 23, 4, 10]
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    my_tree = build_tree(numbers)

    # Search for a node in the BST
    print(my_tree.Search(10))

    # 1. in_order_traversal(): perofrms in order traversal of a binary tree
    print(my_tree.in_order_traversal())

    # 2. find_min(): finds minimum element in entire binary tree
    print(my_tree.find_min())

    # 3. find_max(): finds maximum element in entire binary tree
    print(my_tree.find_max())

    # 4. calculate_sum(): calcualtes sum of all elements
    print(my_tree.calculate_sum())

    # 5. post_order_traversal(): performs post order traversal of a binary tree
    print(my_tree.post_order_traversal())

    # 6. pre_order_traversal(): perofrms pre order traversal of a binary tree
    print(my_tree.pre_order_traversal())

    # 7. Delete a node(no child--one child--two child)
    print(my_tree.in_order_traversal())
    my_tree.delete_node(17)
    print(my_tree.in_order_traversal())

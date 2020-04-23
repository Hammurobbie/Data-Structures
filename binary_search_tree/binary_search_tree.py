from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            self.right = value
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        if self.value is not None:
            cb(self.value)
            if self.left is not None:
                self.left.for_each(cb)
            if self.right is not None:
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        if node is None:
            return
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            cur = q.dequeue()
            print(cur.value)
            if cur.left:
                q.enqueue(cur.left)
            if cur.right:
                q.enqueue(cur.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        if node.left is not None:
            node.left.dft_print(node.left)
        if node.right is not None:
            node.right.dft_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(9)

bst.insert(2)
bst.insert(5)
bst.insert(3)
bst.insert(11)


bst.in_order_print(1)

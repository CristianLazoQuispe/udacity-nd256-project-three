class EmptyHaystack(Exception):
    pass


class UdacityLies(Exception):
    pass


class Node(object):
    # Because magic strings are the devil's playground
    BLACK = 'black'
    RED = 'red'

    def __init__(self, color, value, index, parent):
        self.color = color
        self.index = index
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def grandparent(self):
        """
        Convenience method, to return a node's grandparent

        :return: Node|None
        """
        return None if self.is_root() else self.parent.parent

    def is_root(self):
        """
        Return a boolean indicating whether this is a root node

        :return: bool
        """
        return self.parent is None

    def sibling(self):
        """
        Return the node's sibling, if it exists

        :return: Node|None
        """
        if self.is_root():
            return None
        if self is self.parent.left:
            return self.parent.right
        if self is self.parent.right:
            return self.parent.left


class RedBlackTree(object):
    def __init__(self, root_value):
        self.root = Node(Node.RED, root_value, 0, None)

    @staticmethod
    def make(values):
        """
        Construct a new red-black tree from a list of values

        :param values: a list of values
        :return: RedBlackTree
        """
        root, *values = values
        tree = RedBlackTree(root)

        for index in range(len(values)):
            tree.insert(values[index], index + 1)

        return tree

    def insert(self, value, index):
        """
        Insert the given value in the self-balancing tree

        :param value: int
        :param index: int
        """

        def find_home(node, value, index):
            """
            Find a home for the given value

            :param node: Node
            :param value: int
            :param index: int
            :return: Node
            """
            if value == node.value:
                # You said we could assume there are no duplicates, Udacity
                raise UdacityLies()

            if value < node.value:
                if node.left:
                    return find_home(node.left, value, index)
                else:
                    node.left = Node(Node.RED, value, index, node)
                    return node.left

            if value > node.value:
                if node.right:
                    return find_home(node.right, value, index)
                else:
                    node.right = Node(Node.RED, value, index, node)
                    return node.right

        new_node = find_home(self.root, value, index)
        self.rebalance(new_node)

    def rebalance(self, node):
        """
        Rebalance the tree using MAGIC, and confusing algorithms

        :param node: Node
        """

        def rotate_left(node):
            # We're rotating a sub-tree. Make a note of the parent, before this all becomes too confusing.
            parent = node.parent

            node_up = node.right
            node.right = node_up.left
            node_up.left = node
            node.parent = node_up

            if parent:
                if node is parent.left:
                    parent.left = node_up
                else:
                    parent.right = node_up

            node_up.parent = parent

        def rotate_right(node):
            # We're rotating a sub-tree. Make a note of the parent, before this all becomes too confusing.
            parent = node.parent

            node_up = node.left
            node.left = node_up.right
            node_up.right = node
            node.parent = node_up

            if parent:
                if node is parent.left:
                    parent.left = node_up
                else:
                    parent.right = node_up

            node_up.parent = parent

        # ------------------------------------------
        # Case 1: this is the root node.
        # ------------------------------------------
        if node.is_root():
            node.color = Node.BLACK
            return

        # We're going to be using this a lot.
        parent = node.parent

        # ------------------------------------------
        # Case 2: a black parent node.
        # ------------------------------------------
        if parent.color is Node.BLACK:
            return

        grandparent = node.grandparent()
        uncle = node.parent.sibling()

        # ------------------------------------------
        # Case 3: the parent and uncle are both red.
        # ------------------------------------------
        if grandparent and uncle:
            # We've already checked the parent colour once, but let's do it again, for clarity.
            if parent.color is Node.RED and uncle.color is Node.RED:
                parent.color = Node.BLACK
                uncle.color = Node.BLACK
                grandparent.color = Node.RED
                return self.rebalance(grandparent)

        # No, pop-pop means we're done.
        if grandparent is None:
            return

        # -----------------------------------------------------
        # Cases 4 and 5: the parent is red, the uncle is black.
        # -----------------------------------------------------
        # Case 4: the node is on the inside of the sub-tree.
        if grandparent.left and grandparent.left.right is node:
            rotate_left(parent)
            node = node.left
        elif grandparent.right and grandparent.right.left is node:
            rotate_right(parent)
            node = node.right

        # Reassign the variables after rotating.
        parent = node.parent
        grandparent = node.grandparent()

        # Case 5: the node is on the outside of the sub-tree.
        if grandparent.left and grandparent.left.left is node:
            rotate_right(grandparent)
        elif grandparent.right and grandparent.right.right is node:
            rotate_left(grandparent)

        # Fix the colours, after all that rotating.
        parent.color = Node.BLACK
        grandparent.color = Node.RED

    def find(self, value):
        """
        Find the given value in the tree, and return the associated Node

        If the value cannot be found, return None

        :param value: int
        :return: Node|None
        """

        def recurse(node, value):
            if node.value == value:
                return node
            if value < node.value:
                return recurse(node.left, value) if node.left else None
            if value > node.value:
                return recurse(node.right, value) if node.right else None

        return recurse(self.root, value)


def rotated_array_search(haystack, needle):
    """
    Find the given needle in the given haystack

    If the needle is found, return its index. If it cannot be found, return -1

    :param haystack: the list to search
    :param needle: the value to find
    :return: the value index, or -1
    """
    if not haystack:
        raise EmptyHaystack()

    node = (RedBlackTree.make(haystack)).find(needle)
    return -1 if node is None else node.index


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------
assert rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6) == 0
assert rotated_array_search([5, 7, 100, -1, 6, 3, 12, 19, 46, 2], -1) == 3
assert rotated_array_search([1, 2, 3, 4, 5], 6) == -1

try:
    rotated_array_search([], 12)
    assert False, 'Attempting to create an empty haystack should raise an EmptyHaystack exception'
except EmptyHaystack:
    assert True

try:
    rotated_array_search([1, 1], 1)
    assert False, 'Attempting to create a haystack containing duplicate values should raise an UdacityLies exception'
except UdacityLies:
    assert True

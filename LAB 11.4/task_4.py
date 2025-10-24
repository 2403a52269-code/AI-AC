class Node:
    """Node for a Binary Search Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """A Binary Search Tree (BST) implementation with insertion, search, and inorder traversal."""

    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, value):
        """Insert a value into the BST.

        Args:
            value: The value to be inserted.
        """
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            # Ignore duplicates
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        """Search for a value in the BST.

        Args:
            value: The value to search for.

        Returns:
            bool: True if value is found, False otherwise.
        """
        def _search(node, value):
            if node is None:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    def inorder_traversal(self):
        """Perform an inorder traversal of the BST.

        Returns:
            list: Sorted list of all values in the BST.
        """
        result = []

        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return result

# Test the BST implementation
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [7, 3, 9, 1, 5, 8, 10]
    for v in values:
        bst.insert(v)

    print("Inorder traversal (should be sorted):", bst.inorder_traversal())

    # Test search for present elements
    for elem in [1, 5, 7, 10]:
        print(f"Searching for {elem}: {bst.search(elem)}")  # Expect True

    # Test search for absent elements
    for elem in [0, 4, 11]:
        print(f"Searching for {elem}: {bst.search(elem)}")  # Expect False

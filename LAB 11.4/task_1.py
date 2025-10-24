class Stack:
    """A simple Stack (LIFO) implementation in Python.

    Provides push, pop, peek, and is_empty methods.

    Attributes:
        items (list): Internal container to store stack elements.
    """

    def __init__(self):
        """Initializes an empty stack."""

        self.items = []

    def push(self, item):
        """Push an item onto the stack.

        Args:
            item: The data to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack.

        Returns:
            The last pushed item.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item from the stack without removing it.

        Returns:
            The last pushed item.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0


if __name__ == '__main__':
    # Test the Stack class
    stack = Stack()
    print("Is stack empty?", stack.is_empty())  # True

    sample_data = [1, 2, 3, 4]
    print("Pushing data:", sample_data)
    for val in sample_data:
        stack.push(val)
        print(f"Pushed {val}, Top is now: {stack.peek()}")

    print("Is stack empty?", stack.is_empty())  # False

    print("Popping all items:")
    while not stack.is_empty():
        top_val = stack.pop()
        print(f"Popped {top_val}")

    print("Is stack empty after pops?", stack.is_empty())  # True

    # Uncomment the following lines to see error handling
    # stack.pop()  # Should raise IndexError
    # stack.peek() # Should raise IndexError

    print("\nSuggestion: For improved performance with very large stacks or frequent insertions/deletions at both ends, consider using `collections.deque` from Python's standard library as the underlying container. It provides O(1) time complexity for append and pop operations from both ends, whereas list's pop(0) is O(n). However, for LIFO stacks using append() and pop(), list is efficient for most common use cases.")

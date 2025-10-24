class Node:
    """A node in a singly linked list."""
    def __init__(self, value):
        self.value = value    # The value held by the node
        self.next = None      # Pointer to the next node
class LinkedList:
    """Singly linked list with insertion, deletion, and traversal."""
    def __init__(self):
        self.head = None  # Start with an empty list
    def insert_at_end(self, value):
        """Insert a new node with the given value at the end of the list."""
        new_node = Node(value)
        if not self.head:
            # If the list is empty, new node becomes the head
            self.head = new_node
        else:
            # Traverse to the last node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete_value(self, value):
        """Delete the first occurrence of value in the list."""
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev is None:
                    # Deleting the head node
                    self.head = current.next
                else:
                    prev.next = current.next
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found
    def traverse(self):
        """Return a list of all values in linked list order."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next  # Move to the next node
        return result

# ----- AI TEST CASE SUGGESTIONS -----
# 1. Insert several values and traverse to check order.
# 2. Delete head value, middle value, tail value, and a missing value.
# 3. Delete the only value in a single-node list.
# 4. Traverse an empty list.
# 5. Insert after deletions to verify list integrity.

if __name__ == "__main__":
    # Create empty list, traverse
    ll = LinkedList()
    print("Initial empty list:", ll.traverse())  # []

    # Insert values
    for val in [10, 20, 30, 40]:
        ll.insert_at_end(val)
    print("List after insertions:", ll.traverse())  # [10, 20, 30, 40]

    # Delete head
    ll.delete_value(10)
    print("After deleting head (10):", ll.traverse())  # [20, 30, 40]

    # Delete middle
    ll.delete_value(30)
    print("After deleting middle (30):", ll.traverse())  # [20, 40]

    # Delete tail
    ll.delete_value(40)
    print("After deleting tail (40):", ll.traverse())  # [20]

    # Delete only remaining value
    ll.delete_value(20)
    print("After deleting sole remaining value (20):", ll.traverse())  # []

    # Try deleting from empty list (should do nothing)
    print("Delete from empty (returns):", ll.delete_value(99))  # False

    # Insert into empty list again
    ll.insert_at_end(55)
    print("Insert into empty list:", ll.traverse())  # [55]

    # Delete missing value
    print("Delete missing value (returns):", ll.delete_value(100))  # False
    print("List after attempting to delete missing value:", ll.traverse())  # [55]

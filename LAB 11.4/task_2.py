class QueueList:
    """A simple queue implementation using Python lists."""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  # O(n) operation

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def __repr__(self):
        return f"QueueList({self.items})"


#performance review and optimization:
print(
    "Performance review:\n"
    "- This QueueList implementation uses a Python list internally. "
    "While enqueue (append) is O(1), dequeue (pop(0)) is O(n) because it shifts all "
    "remaining elements. This can be inefficient for large queues or frequent dequeues.\n"
    "Suggestion: Use collections.deque for optimized O(1) enqueue and dequeue.\n"
)


# Improved version using collections.deque
from collections import deque

class QueueDeque:
    """A queue implementation using collections.deque for O(1) enqueue and dequeue."""
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()  # O(1) operation

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def __repr__(self):
        return f"QueueDeque({list(self.items)})"

#test cases:
if __name__ == "__main__":
    # Test the QueueDeque class
    q = QueueDeque()
    print("Is queue empty?", q.is_empty())  # True

    sample_data = [1, 2, 3, 4]
    print("Enqueuing data:", sample_data)
    for val in sample_data:
        q.enqueue(val)
        print(f"Enqueued {val}, Front is now: {q.items[0]}")

    print("Is queue empty?", q.is_empty())  # False

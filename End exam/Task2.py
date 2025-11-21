"""
Queue Data Structure Implementation
Includes a basic Queue and a BoundedQueue with maximum size constraint.
"""


class Queue:
    """A basic FIFO (First-In-First-Out) queue implementation."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The element to add to the queue.
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        
        Returns:
            The front item of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if len(self.items) == 0:
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)
    
    def front(self):
        """
        Return the front item without removing it.
        
        Returns:
            The front item of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if len(self.items) == 0:
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)
    
    """
Below is the FEW-SHOT prompt used to instruct the AI to modify the Queue:

Few-Shot Learning Examples:

Example 1:
Input: "Add a size() method to the class."
Output: The AI adds:
    def size(self): return len(self.items)

Example 2:
Input: "Make the queue raise an exception when dequeue is called on an empty queue."
Output: The AI adds:
    if not self.items: raise IndexError("Empty queue")

--- Final Instruction ---
"Modify the Queue class to create BoundedQueue(max_size) which:
 - accepts a max_size in constructor
 - prevents enqueue when full
 - raises an Exception('Queue is full') if enqueue exceeds max_size"
"""


class BoundedQueue(Queue):
    """A queue with a maximum size limit (bounded queue)."""
    
    def __init__(self, max_size):
        """
        Initialize a bounded queue with a maximum size.
        
        Args:
            max_size: The maximum number of items the queue can hold.
            
        Raises:
            ValueError: If max_size is less than 1.
        """
        super().__init__()
        if max_size < 1:
            raise ValueError("max_size must be at least 1")
        self.max_size = max_size
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The element to add to the queue.
            
        Raises:
            OverflowError: If the queue is already at maximum capacity.
        """
        if len(self.items) >= self.max_size:
            raise OverflowError(f"Queue is full (max size: {self.max_size})")
        super().enqueue(item)
    
    def is_full(self):
        """Check if the queue is at maximum capacity."""
        return len(self.items) >= self.max_size


# Test cases
if __name__ == "__main__":
    # Test basic Queue
    print("=== Basic Queue Tests ===")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Front: {q.front()}")  # Output: 1
    print(f"Dequeue: {q.dequeue()}")  # Output: 1
    print(f"Size: {q.size()}")  # Output: 2
    
    #test cases using pytest
    import pytest   
    def test_queue_operations():
        queue = Queue()
        assert queue.is_empty() == True
        queue.enqueue(10)
        queue.enqueue(20)
        assert queue.size() == 2
        assert queue.front() == 10
        assert queue.dequeue() == 10
        assert queue.size() == 1
        assert queue.is_empty() == False
        assert queue.dequeue() == 20
        assert queue.is_empty() == True
        with pytest.raises(IndexError):
            queue.dequeue()
        with pytest.raises(IndexError):
            queue.front()
    test_queue_operations()
    # Test BoundedQueue
    print("\n=== Bounded Queue Tests ===")
    bq = BoundedQueue(2)
    bq.enqueue(1)
    bq.enqueue(2)
    print(f"Is full: {bq.is_full()}")  # Output: True
    try:
        bq.enqueue(3)  # Should raise OverflowError
    except OverflowError as e:
        print(e)  # Output: Queue is full (max size: 2)
    print(f"Dequeue: {bq.dequeue()}")  # Output: 1
    print(f"Is full: {bq.is_full()}")  # Output: False
    def test_bounded_queue_operations():
        bqueue = BoundedQueue(2)
        assert bqueue.is_empty() == True
        bqueue.enqueue(10)
        bqueue.enqueue(20)
        assert bqueue.size() == 2
        assert bqueue.is_full() == True
        with pytest.raises(OverflowError):
            bqueue.enqueue(30)
        assert bqueue.front() == 10
        assert bqueue.dequeue() == 10
        assert bqueue.size() == 1
        assert bqueue.is_full() == False
        assert bqueue.dequeue() == 20
        assert bqueue.is_empty() == True
        with pytest.raises(IndexError):
            bqueue.dequeue()    
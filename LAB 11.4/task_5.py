class Graph:
    """Graph data structure using an adjacency list."""

    def __init__(self):
        # Each key is a node; value is a list of neighbors.
        self.adj_list = {}

    def add_edge(self, src, dest, bidirectional=False):
        """Add an edge from src to dest. Add dest->src if bidirectional (undirected)."""
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(dest)
        if bidirectional:
            self.adj_list[dest].append(src)

    def bfs(self, start):
        """
        Breadth-First Search traversal from start node.
        Returns: List of nodes in BFS order.
        """
        from collections import deque  # Omit if top-level imports are required.
        visited = set()  # Track visited nodes.
        queue = deque([start])  # Queue for BFS.
        result = []

        # AI Explanation: BFS explores neighbors level-by-level using a queue.
        while queue:
            node = queue.popleft()
            if node not in visited:
                result.append(node)  # Visit node
                visited.add(node)
                # Enqueue unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs_iterative(self, start):
        """
        Iterative Depth-First Search traversal from start node.
        Returns: List of nodes in DFS order.
        """
        visited = set()
        stack = [start]
        result = []

        # AI Explanation: DFS uses a stack to go as deep as possible before backtracking
        while stack:
            node = stack.pop()
            if node not in visited:
                result.append(node)
                visited.add(node)
                # Push neighbors in reverse for correct left-to-right traversal order
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def dfs_recursive(self, start):
        """
        Recursive Depth-First Search traversal from start node.
        Returns: List of nodes in DFS order.
        """
        visited = set()
        result = []

        def dfs(node):
            # Visit and record node, then all neighbors recursively
            if node not in visited:
                result.append(node)
                visited.add(node)
                for neighbor in self.adj_list.get(node, []):
                    dfs(neighbor)

        dfs(start)
        return result

    def dfs(self, start, method="iterative"):
        """
        General DFS interface: allows choosing recursive or iterative method.
        """
        if method == "recursive":
            return self.dfs_recursive(start)
        return self.dfs_iterative(start)


# --- AI Commentary on Recursive vs Iterative DFS ---
# Recursive DFS is concise but can hit recursion limits for deep/large graphs.
# Iterative DFS (using a stack) avoids recursion depth issues and is preferred for large graphs in production.

# ----------- Example/Test code for demonstration -----------
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge(0, 1, bidirectional=True)
    g.add_edge(0, 2, bidirectional=True)
    g.add_edge(1, 3, bidirectional=True)
    g.add_edge(1, 4, bidirectional=True)
    g.add_edge(2, 5, bidirectional=True)
    g.add_edge(4, 5, bidirectional=True)

    print("Adjacency List:")
    for node in g.adj_list:
        print(f"{node}: {g.adj_list[node]}")

    print("\nBFS Traversal from node 0:", g.bfs(0))
    print("DFS Iterative Traversal from node 0:", g.dfs(0, method='iterative'))
    print("DFS Recursive Traversal from node 0:", g.dfs(0, method='recursive'))

    # AI Suggestion: For small graphs, both DFS versions yield the same order (if neighbor order is identical).
    # For very large graphs or with limited recursion stack, prefer the iterative version.


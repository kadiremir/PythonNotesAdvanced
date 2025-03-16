"""2025, Kadir Emir, https://github.com/kadiremir"""

from collections import deque


class GraphSearch:

    def dfs_recursive(self, graph, node, visited=None):
        """Depth First Search (DFS) algorithm using recursion."""
        if visited is None:
            visited = set()

        visited.add(node)
        print(node, end=" ")  # Process the node

        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs_recursive(graph, neighbor, visited)

    def dfs_iterative(self, graph, start):
        """Depth First Search (DFS) algorithm using iteration."""
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                stack.extend(reversed(graph[node]))  # Reverse to maintain order

    def bfs(self, graph, start):
        """Breadth First Search (BFS) algorithm."""
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(graph[node])  # Add neighbors to the queue


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}


if __name__ == '__main__':
    print("DFS Recursive:")
    GraphSearch().dfs_recursive(graph, 'A')

    print("\nDFS Iterative:")
    GraphSearch().dfs_iterative(graph, 'A')

    print("\nBFS:")
    GraphSearch().bfs(graph, 'A')
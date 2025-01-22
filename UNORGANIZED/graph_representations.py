def get_dictionary_representation_of_graph(graph: list[list[int]]) -> dict:
    """Returns the dictionary representation of a graph."""
    graph_dict = {}

    for edge in graph:
        # Ensure both the source and destination nodes are in the dictionary
        if edge[0] not in graph_dict:
            graph_dict[edge[0]] = []
        if edge[1] not in graph_dict:
            graph_dict[edge[1]] = []

        # Add the destination to the adjacency list of the source
        graph_dict[edge[0]].append(edge[1])

    return graph_dict

def get_all_connections_of_a_node(graph: dict[int, list[int]], node: int) -> list[int]:
    """Returns all possibe nodes connected walktrough the given node."""
    visited = set()
    stack = [node]

    while stack:
        current_node = stack.pop()
        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return list(visited)


my_graph = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]
print(get_dictionary_representation_of_graph(my_graph))
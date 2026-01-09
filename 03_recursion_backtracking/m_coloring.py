def color_graph(graph, m):
    """
    Return all valid colorings for the given graph using at most m colors.
    Graph is a dict {node: [neighbors]}. Colors are numbered 1..m.
    """
    nodes = list(graph.keys())
    colors = {}
    solutions = []

    def is_safe(node, color):
        return all(colors.get(neighbor) != color for neighbor in graph[node])

    def backtrack(index):
        if index == len(nodes):
            solutions.append(colors.copy())
            return

        node = nodes[index]
        for color in range(1, m + 1):
            if is_safe(node, color):
                colors[node] = color
                backtrack(index + 1)
                del colors[node]

    backtrack(0)
    return solutions


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"],
    }

    max_colors = 3
    solutions = color_graph(graph, max_colors)
    if solutions:
        print(f"Found {len(solutions)} valid colorings with {max_colors} colors:")
        for coloring in solutions:
            print(coloring)
    else:
        print(f"No valid coloring exists with {max_colors} colors.")

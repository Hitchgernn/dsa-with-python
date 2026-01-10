def hamiltonian_cycle(graph):
    """
    Return one Hamiltonian cycle for the given graph as a list of vertices.
    Graph is an adjacency matrix: graph[i][j] == 1 means edge exists.
    """
    n = len(graph)
    if n == 0:
        return []

    path = [-1] * n
    path[0] = 0

    def is_safe(v, pos):
        if graph[path[pos - 1]][v] == 0:
            return False
        return v not in path[:pos]

    def backtrack(pos):
        if pos == n:
            return graph[path[pos - 1]][path[0]] == 1

        for v in range(1, n):
            if is_safe(v, pos):
                path[pos] = v
                if backtrack(pos + 1):
                    return True
                path[pos] = -1
        return False

    if backtrack(1):
        return path + [path[0]]
    return []


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]

    cycle = hamiltonian_cycle(graph)
    if cycle:
        print("Hamiltonian Cycle:", cycle)
    else:
        print("No Hamiltonian Cycle found.")

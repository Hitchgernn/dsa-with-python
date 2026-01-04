def find_paths(maze):
    """
    Return all valid paths for the Rat in a Maze problem.
    1 = open cell, 0 = blocked. Start at (0,0), goal at bottom-right.
    Paths are encoded as strings of moves: D, R, U, L.
    """
    if not maze or not maze[0]:
        return []

    rows, cols = len(maze), len(maze[0])
    if maze[0][0] == 0 or maze[rows - 1][cols - 1] == 0:
        return []

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    moves = [(1, 0, "D"), (0, 1, "R"), (-1, 0, "U"), (0, -1, "L")]
    path = []
    paths = []

    def backtrack(r, c):
        if r == rows - 1 and c == cols - 1:
            paths.append("".join(path))
            return

        visited[r][c] = True
        for dr, dc, move in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1 and not visited[nr][nc]:
                path.append(move)
                backtrack(nr, nc)
                path.pop()
        visited[r][c] = False

    backtrack(0, 0)
    return paths


if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1],
    ]

    solutions = find_paths(maze)
    print("Solutions:", solutions if solutions else "No path found")

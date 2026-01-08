def solve_n_queens(n):
    """
    Return all solutions for the N-Queens problem.
    Each solution is a list of strings with 'Q' and '.'.
    """
    if n <= 0:
        return []

    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(r):
        if r == n:
            solutions.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            board[r][c] = "Q"

            backtrack(r + 1)

            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return solutions


if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    if solutions:
        print(f"Found {len(solutions)} solutions for {n}-Queens:")
        for board in solutions:
            for row in board:
                print(row)
            print()
    else:
        print(f"No solutions found for {n}-Queens.")

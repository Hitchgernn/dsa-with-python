def combination_sum(candidates, target):
    """
    Return all unique combinations where numbers sum to target.
    Each number in candidates may be used unlimited times.
    """
    candidates = sorted(candidates)
    solutions = []
    combo = []

    def backtrack(start, total):
        if total == target:
            solutions.append(combo.copy())
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            num = candidates[i]
            combo.append(num)
            backtrack(i, total + num)
            combo.pop()

    backtrack(0, 0)
    return solutions


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    solutions = combination_sum(candidates, target)
    if solutions:
        print(f"Combinations of {candidates} that sum to {target}:")
        for s in solutions:
            print(s)
    else:
        print(f"No combinations sum to {target}.")

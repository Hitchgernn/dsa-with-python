def subset_sum(nums, target):
    """
    Return all subsets that sum to target.
    Each subset is represented as a list of numbers.
    """
    solutions = []
    subset = []

    def backtrack(index, total):
        if total == target:
            solutions.append(subset.copy())
            return
        if index == len(nums) or total > target:
            return

        # include current
        subset.append(nums[index])
        backtrack(index + 1, total + nums[index])
        subset.pop()

        # exclude current
        backtrack(index + 1, total)

    backtrack(0, 0)
    return solutions


if __name__ == "__main__":
    nums = [2, 3, 5, 6, 8, 10]
    target = 10
    solutions = subset_sum(nums, target)
    if solutions:
        print(f"Subsets of {nums} that sum to {target}:")
        for s in solutions:
            print(s)
    else:
        print(f"No subset sums to {target}.")

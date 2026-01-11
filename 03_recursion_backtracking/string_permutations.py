def string_permutations(s):
    """
    Return all permutations of the given string.
    """
    chars = list(s)
    results = []

    def backtrack(start):
        if start == len(chars):
            results.append("".join(chars))
            return

        for i in range(start, len(chars)):
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]

    backtrack(0)
    return results


if __name__ == "__main__":
    s = "ABC"
    perms = string_permutations(s)
    print(f"Permutations of {s}:")
    for p in perms:
        print(p)

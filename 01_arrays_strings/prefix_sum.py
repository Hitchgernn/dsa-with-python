def build_prefix_sum(nums):
    """
    Return prefix sum array where prefix[i] is sum of nums[0..i].
    """
    prefix = []
    running = 0
    for num in nums:
        running += num
        prefix.append(running)
    return prefix


def range_sum(prefix, left, right):
    """
    Return sum of nums[left..right] using prefix array.
    """
    if left < 0 or right < 0 or left > right:
        return None
    return prefix[right] - (prefix[left - 1] if left > 0 else 0)


if __name__ == "__main__":
    nums = [2, 4, 5, 7, 1, 3]
    prefix = build_prefix_sum(nums)
    print("nums:", nums)
    print("prefix:", prefix)
    print("sum 1..3:", range_sum(prefix, 1, 3))

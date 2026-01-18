def max_sum_subarray(nums, k):
    if k <= 0 or k > len(nums):
        return None
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum


def longest_substring_no_repeat(s):
    last_seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


def min_size_subarray_sum(nums, target):
    left = 0
    curr = 0
    best = None
    for right, val in enumerate(nums):
        curr += val
        while curr >= target:
            window_len = right - left + 1
            best = window_len if best is None else min(best, window_len)
            curr -= nums[left]
            left += 1
    return best


if __name__ == "__main__":
    print("max_sum_subarray:", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
    print("longest_substring_no_repeat:", longest_substring_no_repeat("abcabcbb"))
    print("min_size_subarray_sum:", min_size_subarray_sum([2, 3, 1, 2, 4, 3], 7))

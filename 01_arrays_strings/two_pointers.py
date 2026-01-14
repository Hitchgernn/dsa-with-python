def reverse_list(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


def reverse_string(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


def remove_duplicates_sorted(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def move_zeros(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums


def pair_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1
    return None


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("reverse_list:", reverse_list(nums.copy()))
    print("reverse_string:", reverse_string("ABCDE"))

    dup_nums = [1, 1, 2, 2, 3, 4, 4]
    new_len = remove_duplicates_sorted(dup_nums)
    print("remove_duplicates_sorted:", dup_nums[:new_len], "len:", new_len)

    zeros = [0, 1, 0, 3, 12]
    print("move_zeros:", move_zeros(zeros))

    pair_nums = [1, 2, 4, 6, 10]
    print("pair_sum_sorted (target 8):", pair_sum_sorted(pair_nums, 8))

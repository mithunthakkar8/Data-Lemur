def sorted_two_sum(nums, target):
    nums_seen = {}
    for i, num_2 in enumerate(nums):
        num_1 = target - num_2
        if num_1 in nums_seen:
            return [nums_seen[num_1], i]
        nums_seen[num_2] = i
    return [-1, -1]

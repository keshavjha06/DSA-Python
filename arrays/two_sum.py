def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def two_sum_hashmap(nums, target):
    seen = {}  # value -> index
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return [seen[needed], i]
        seen[nums[i]] = i
    return [0, 0]


nums = [7, 11, 2, 5, 4, 6]
target = 10
print(two_sum_brute_force(nums, target))
print(two_sum_hashmap(nums, target))

def max_sub_array(nums):
    total = 0
    max_sum = nums[0]
    for i in range(len(nums)):
        total = total + nums[i]
        if total > max_sum:
            max_sum = total
        if total < 0:
            total = 0
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(nums))

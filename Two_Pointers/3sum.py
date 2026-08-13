
def three_sum(nums):
    solutions = []

    nums = sorted(nums)

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = num + nums[left] + nums[right]
            if total == 0:
                solutions.append([num, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return solutions

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1

    

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))
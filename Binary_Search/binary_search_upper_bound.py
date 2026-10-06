vec = [4, 222, 1,2, 4, 2, 5, 2, 8]
vec.sort()

print(vec)

left = 0
right = len(vec)
target = 2

while left < right:
    mid = (left + right) // 2

    if target < vec[mid]:
        right = mid
    else:
        left = mid + 1

print(left)
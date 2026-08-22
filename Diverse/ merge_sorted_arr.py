class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        k = 0
        new_arr = [0] * (m + n)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                new_arr[k] = nums1[i]
                i += 1
                k += 1
            else:
                new_arr[k] = nums2[j]
                j += 1
                k += 1

        while i < m:
            new_arr[k] = nums1[i]
            i += 1
            k += 1
        
        while j < n:
            new_arr[k] = nums2[j]
            j += 1
            k += 1

        nums1[:] = new_arr
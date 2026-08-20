int comp(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

int maxOperations(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(nums[0]), comp);

    int left = 0;
    int right = numsSize - 1;
    int count = 0;

    while (left < right) {
        int total = nums[left] + nums[right];

        if (total == k) {
            count++;
            left++;
            right--;
        } else if (total < k) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}
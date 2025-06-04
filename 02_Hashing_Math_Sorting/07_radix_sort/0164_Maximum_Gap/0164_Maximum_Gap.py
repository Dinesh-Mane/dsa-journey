def maximumGap(nums):
    if len(nums) < 2:
        return 0

    def radix_sort(arr):
        max_num = max(arr)
        exp = 1
        base = 10
        while max_num // exp > 0:
            buckets = [[] for _ in range(base)]
            for num in arr:
                buckets[(num // exp) % base].append(num)
            arr = [num for bucket in buckets for num in bucket]
            exp *= base
        return arr

    nums = radix_sort(nums)
    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i - 1])
    return max_gap
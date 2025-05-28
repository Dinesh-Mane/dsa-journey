def twoOutOfThree(nums1, nums2, nums3):
    set1, set2, set3 = set(nums1), set(nums2), set(nums3)
    all_nums = set1 | set2 | set3
    result = []
    for num in all_nums:
        count = (num in set1) + (num in set2) + (num in set3)
        if count >= 2:
            result.append(num)
    return result
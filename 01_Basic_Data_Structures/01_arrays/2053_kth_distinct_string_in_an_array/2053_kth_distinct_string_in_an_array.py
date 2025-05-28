from collections import Counter

def kthDistinct(arr, k):
    freq = Counter(arr)
    for word in arr:
        if freq[word] == 1:
            k -= 1
            if k == 0:
                return word
    return ""
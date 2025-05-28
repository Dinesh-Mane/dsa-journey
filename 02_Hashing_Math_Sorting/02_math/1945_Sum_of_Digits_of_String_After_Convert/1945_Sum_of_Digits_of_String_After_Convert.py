def getLucky(s, k):
    total = sum(int(d) for c in s for d in str(ord(c) - 96))
    for _ in range(k - 1):
        total = sum(int(d) for d in str(total))
    return total
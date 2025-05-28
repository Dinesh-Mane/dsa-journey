def numOfStrings(patterns, word):
    count = 0
    for p in patterns:
        if p in word:
            count += 1
    return count
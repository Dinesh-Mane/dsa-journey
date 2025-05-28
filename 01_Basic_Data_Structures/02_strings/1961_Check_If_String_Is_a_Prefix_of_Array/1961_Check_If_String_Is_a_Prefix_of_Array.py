def isPrefixString(s, words):
    i = 0
    for word in words:
        if s[i:i+len(word)] != word:
            return False
        i += len(word)
        if i == len(s):
            return True
    return False
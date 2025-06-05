def smallestEquivalentString(s1, s2, baseStr):
    parent = list(range(26))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            if pa < pb: parent[pb] = pa
            else: parent[pa] = pb
    for a, b in zip(s1, s2):
        union(ord(a)-97, ord(b)-97)
    return ''.join(chr(find(ord(c)-97)+97) for c in baseStr)
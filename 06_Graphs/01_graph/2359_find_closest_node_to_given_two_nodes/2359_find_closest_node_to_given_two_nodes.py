def closestMeetingNode(e, n1, n2):
    def dist(start):
        d = {}
        s, l = start, 0
        while s != -1 and s not in d:
            d[s] = l
            s = e[s]
            l += 1
        return d

    d1, d2 = dist(n1), dist(n2)
    res, min_d = -1, float('inf')
    for i in range(len(e)):
        if i in d1 and i in d2:
            m = max(d1[i], d2[i])
            if m < min_d or (m == min_d and i < res):
                res, min_d = i, m
    return res
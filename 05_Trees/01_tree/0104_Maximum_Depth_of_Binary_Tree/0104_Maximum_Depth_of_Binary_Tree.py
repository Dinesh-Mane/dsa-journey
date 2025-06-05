def maxDepth(r):
    if not r: return 0
    return 1 + max(maxDepth(r.left), maxDepth(r.right))
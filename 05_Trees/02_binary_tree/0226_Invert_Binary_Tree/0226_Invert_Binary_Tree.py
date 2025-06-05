def inv(r):
    if r:
        r.left, r.right = inv(r.right), inv(r.left)
    return r
def pt(k):
    row = [1]
    for _ in range(k):
        row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
    return row
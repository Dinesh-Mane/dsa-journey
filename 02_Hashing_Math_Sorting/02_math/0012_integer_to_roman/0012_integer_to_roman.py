def intToRoman(num):
    val_sym = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    )
    res = ""
    for val, sym in val_sym:
        count, num = divmod(num, val)
        res += sym * count
    return res
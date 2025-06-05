def cs(n, dp={}):
    if n in dp: return dp[n]
    if n <= 2: return n
    dp[n] = cs(n-1, dp) + cs(n-2, dp)
    return dp[n]
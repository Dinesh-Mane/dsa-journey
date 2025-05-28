def strStr(haystack: str, needle: str) -> int:
  def buildLPS(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of previous longest prefix suffix
    i = 1
    while i < len(pattern):
      if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
      else:
        if length != 0: length = lps[length - 1]  # fallback
        else:
          lps[i] = 0
          i += 1
    return lps

  if not needle: return 0
  lps = buildLPS(needle)
  i = j = 0  # i for haystack, j for needle

  while i < len(haystack):
    if haystack[i] == needle[j]:
      i += 1
      j += 1
      if j == len(needle): return i - j
      else:
        if j != 0: j = lps[j - 1]  # fallback
        else: i += 1
  return -1
class Solution:
  def maxProduct(self, s: str) -> int:
    kBase = 26
    kMod = int(1e9) + 7
    n = len(s)
    ans = 1
    pow = [1] + [0] * n  # pow[i] := kBase^i
    hashFromLeft = [0] * (n + 1)  # hashFromLeft[i] = hash value of s[0..i)
    hashFromRight = [0] * (n + 1)  # hashFromRight[i] = hash value of s[i..n)
    l = [0] * n  # l[i] := max length of palindromes in s[0..i)
    r = [0] * n  # r[i] := max length of palindromes in s[i..n)

    for i in range(1, n + 1):
      pow[i] = pow[i - 1] * kBase % kMod

    for i in range(1, n + 1):
      hashFromLeft[i] = (hashFromLeft[i - 1] * kBase +
                         ord(s[i - 1]) - ord('a') + 1) % kMod

    for i in range(n - 1, -1, -1):
      hashFromRight[i] = (hashFromRight[i + 1] * kBase +
                          ord(s[i]) - ord('a') + 1) % kMod

    def leftHash(l: int, r: int) -> int:
      hash = (hashFromLeft[r] - hashFromLeft[l] * pow[r - l]) % kMod
      return hash + kMod if hash < 0 else hash

    def rightHash(l: int, r: int) -> int:
      hash = (hashFromRight[l] - hashFromRight[r] * pow[r - l]) % kMod
      return hash + kMod if hash < 0 else hash

    def isPalindrome(l: int, r: int) -> bool:
      return leftHash(l, r) == rightHash(l, r)

    maxi = 1
    for i in range(n):
      if i - maxi - 1 >= 0 and isPalindrome(i - maxi - 1, i + 1):
        maxi += 2
      l[i] = maxi

    maxi = 1
    for i in range(n - 1, -1, -1):
      if i + maxi + 2 <= n and isPalindrome(i, i + maxi + 2):
        maxi += 2
      r[i] = maxi

    for i in range(n - 1):
      ans = max(ans, l[i] * r[i + 1])

    return ans

class Solution:
  def sumSubarrayMins(self, A: List[int]) -> int:
    kMod = int(1e9) + 7
    n = len(A)
    ans = 0
    prev = [-1] * n
    next = [n] * n
    stack = []

    for i, a in enumerate(A):
      while stack and A[stack[-1]] > a:
        index = stack.pop()
        next[index] = i
      if stack:
        prev[i] = stack[-1]
      stack.append(i)

    for i, a in enumerate(A):
      ans = (ans + a * (i - prev[i]) * (next[i] - i)) % kMod

    return ans

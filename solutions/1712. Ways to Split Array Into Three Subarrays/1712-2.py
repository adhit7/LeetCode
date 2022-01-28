class Solution:
  def waysToSplit(self, nums: List[int]) -> int:
    kMod = int(1e9 + 7)
    n = len(nums)
    ans = 0
    prefix = list(itertools.accumulate(nums))

    j = 0
    k = 0
    for i in range(n - 2):
      # find first index j s.t.
      # left = prefix[i] <= mid = prefix[j] - prefix[i]
      while j <= i or (j < n - 1 and prefix[i] > prefix[j] - prefix[i]):
        j += 1
      # find first index k s.t.
      # mid = prefix[k] - prefix[i] > right = prefix[-1] - prefix[k]
      while k < j or (k < n - 1 and prefix[k] - prefix[i] <= prefix[-1] - prefix[k]):
        k += 1
      ans = (ans + k - j) % kMod

    return ans

class Solution:
  def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    ans = []
    threshold = sorted(nums)[-k]
    larger = sum(1 for num in nums if num > threshold)
    equal = k - larger

    for num in nums:
      if num > threshold:
        ans.append(num)
      elif num == threshold and equal:
        ans.append(num)
        equal -= 1

    return ans

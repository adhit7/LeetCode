class Solution:
  def countElements(self, nums: List[int]) -> int:
    mini = min(nums)
    maxi = max(nums)
    return sum(1 for num in nums if mini < num < maxi)

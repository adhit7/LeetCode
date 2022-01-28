class Solution:
  def targetIndices(self, nums: List[int], target: int) -> List[int]:
    count = nums.count(target)
    lessThan = sum(1 for num in nums if num < target)
    return [i for i in range(lessThan, lessThan + count)]

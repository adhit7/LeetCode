class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    first = inf
    second = inf

    for num in nums:
      if num <= first:
        first = num
      elif num <= second:  # first < num <= second
        second = num
      else:
        return True  # first < second < num (third)

    return False

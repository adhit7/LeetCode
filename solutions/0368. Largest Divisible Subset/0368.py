class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = []
    count = [1] * n
    prevIndex = [-1] * n
    maxCount = 0
    index = -1

    nums.sort()

    for i, num in enumerate(nums):
      for j in range(i)[::-1]:
        if num % nums[j] == 0 and count[i] < count[j] + 1:
          count[i] = count[j] + 1
          prevIndex[i] = j
      if count[i] > maxCount:
        maxCount = count[i]
        index = i

    while index != -1:
      ans.append(nums[index])
      index = prevIndex[index]

    return ans

class Solution:
  def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
    @lru_cache
    def dp(mask: int) -> int:
      i = bin(mask).count("1")
      if i == len(nums1):
        return 0
      return min((nums1[i] ^ nums2[j]) + dp(mask | (1 << j))
                 for j in range(len(nums2)) if mask & (1 << j) == 0)
    return dp(0)

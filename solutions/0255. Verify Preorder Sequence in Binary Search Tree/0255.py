class Solution:
  def verifyPreorder(self, preorder: List[int]) -> bool:
    i = 0

    def dfs(min: int, max: int) -> None:
      nonlocal i
      if i == len(preorder):
        return
      if preorder[i] < min or preorder[i] > max:
        return

      val = preorder[i]
      i += 1
      dfs(min, val)
      dfs(val, max)

    dfs(-inf, inf)
    return i == len(preorder)

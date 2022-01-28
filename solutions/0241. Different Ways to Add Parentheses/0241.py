class Solution:
  @lru_cache(None)
  def diffWaysToCompute(self, expression: str) -> List[int]:
    ans = []

    for i, c in enumerate(expression):
      if c in '+-*':
        left = self.diffWaysToCompute(expression[:i])
        right = self.diffWaysToCompute(expression[i + 1:])
        for a in left:
          for b in right:
            ans.append(eval(str(a) + c + str(b)))

    return ans or [int(expression)]

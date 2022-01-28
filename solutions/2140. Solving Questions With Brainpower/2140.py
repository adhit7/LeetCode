class Solution:
  def mostPoints(self, questions: List[List[int]]) -> int:
    n = len(questions)
    # dp[i] := max points starting from questions[i]
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
      points, brainpower = questions[i]
      nextIndex = i + brainpower + 1
      nextPoints = dp[nextIndex] if nextIndex < n else 0
      dp[i] = max(points + nextPoints, dp[i + 1])

    return dp[0]

class Solution:
  def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
    n = len(s)
    ans = []
    closestLeftCandle = [0] * n
    closestRightCandle = [0] * n
    candleCount = [0] * n  # candleCount[i] := # of candles in s[0..i]
    candle = -1
    count = 0

    for i, c in enumerate(s):
      if c == '|':
        candle = i
        count += 1
      closestLeftCandle[i] = candle
      candleCount[i] = count

    candle = -1
    for i in range(n - 1, -1, -1):
      if s[i] == '|':
        candle = i
      closestRightCandle[i] = candle

    for left, right in queries:
      l = closestRightCandle[left]
      r = closestLeftCandle[right]
      if l == -1 or r == -1 or l > r:
        ans.append(0)
      else:
        lengthBetweenCandles = r - l + 1
        numCandles = candleCount[r] - candleCount[l] + 1
        ans.append(lengthBetweenCandles - numCandles)

    return ans

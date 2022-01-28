from sortedcontainers import SortedDict


class Solution:
  def brightestPosition(self, lights: List[List[int]]) -> int:
    ans = inf
    maxBrightness = -1
    currBrightness = 0
    timeline = SortedDict()

    for position, range in lights:
      start = position - range
      end = position + range + 1
      timeline[start] = timeline.get(start, 0) + 1
      timeline[end] = timeline.get(end, 0) - 1

    for pos, brightness in timeline.items():
      currBrightness += brightness
      if currBrightness > maxBrightness:
        maxBrightness = currBrightness
        ans = pos

    return ans

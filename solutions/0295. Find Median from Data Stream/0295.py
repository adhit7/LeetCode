class MedianFinder:
  def __init__(self):
    self.l = []  # max-heap
    self.r = []  # min-heap

  def addNum(self, num: int) -> None:
    if not self.l or num <= -self.l[0]:
      heapq.heappush(self.l, -num)
    else:
      heapq.heappush(self.r, num)

    # balance two heaps s.t. |l| >= |r| and |l| - |r| <= 1
    if len(self.l) < len(self.r):
      heapq.heappush(self.l, -heapq.heappop(self.r))
    elif len(self.l) - len(self.r) > 1:
      heapq.heappush(self.r, -heapq.heappop(self.l))

  def findMedian(self) -> float:
    if len(self.l) == len(self.r):
      return (-self.l[0] + self.r[0]) / 2.0
    return -self.l[0]

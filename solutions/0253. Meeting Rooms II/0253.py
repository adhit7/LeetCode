class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    pq = []  # store end times of each room

    for start, end in sorted(intervals):
      if pq and start >= pq[0]:
        heapq.heappop(pq)
      heapq.heappush(pq, end)

    return len(pq)

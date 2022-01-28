class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = [[] for _ in range(n)]
    pq = [(0, src, k + 1)]  # (dist, u, stops): min-heap sorted by dist
    minDist = [[inf] * (k + 2) for _ in range(n)]

    for u, v, price in flights:
      graph[u].append((v, price))

    while pq:
      dist, u, stops = heapq.heappop(pq)
      if u == dst:
        return dist
      if stops > 0:
        for v, w in graph[u]:
          newDist = dist + w
          if newDist < minDist[v][stops - 1]:
            minDist[v][stops - 1] = newDist
            heapq.heappush(pq, (dist + w, v, stops - 1))

    return -1

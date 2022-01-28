class Solution:
  def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
    graph = [[] for _ in range(n)]
    # (dist, u, d): min-heap sorted by w (d := remaining discounts)
    pq = [(0, 0, discounts)]
    minDiscounts = {}

    for city1, city2, toll in highways:
      graph[city1].append((city2, toll))
      graph[city2].append((city1, toll))

    while pq:
      dist, u, d = heapq.heappop(pq)
      if u == n - 1:
        return dist
      if u in minDiscounts and minDiscounts[u] >= d:
        continue
      minDiscounts[u] = d
      for v, w in graph[u]:
        heapq.heappush(pq, (dist + w, v, d))
        if d > 0:
          heapq.heappush(pq, (dist + w // 2, v, d - 1))

    return -1

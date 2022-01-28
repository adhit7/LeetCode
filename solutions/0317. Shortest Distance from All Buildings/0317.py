class Solution:
  def shortestDistance(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    buildingCount = sum(1 for row in grid for a in row if a == 1)
    dirs = [0, 1, 0, -1, 0]
    ans = inf
    # dist[i][j] := total distance of grid[i][j] (0) to reach all buildings (1)
    dist = [[0] * n for _ in range(m)]
    # reachCount[i][j] := # of building grid[i][j] (0) can reach
    reachCount = [[0] * n for _ in range(m)]

    def bfs(row: int, col: int) -> None:
      q = deque([(row, col)])
      seen = {(row, col)}
      depth = 0

      while q:
        depth += 1
        for _ in range(len(q)):
          i, j = q.popleft()
          for k in range(4):
            x = i + dirs[k]
            y = j + dirs[k + 1]
            if x < 0 or x == m or y < 0 or y == n:
              continue
            if grid[x][y] != 0 or (x, y) in seen:
              continue
            dist[x][y] += depth
            reachCount[x][y] += 1
            q.append((x, y))
            seen.add((x, y))

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:  # bfs from this building
          bfs(i, j)

    for i in range(m):
      for j in range(n):
        if reachCount[i][j] == buildingCount:
          ans = min(ans, dist[i][j])

    return -1 if ans == inf else ans

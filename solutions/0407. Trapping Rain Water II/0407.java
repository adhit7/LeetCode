class T {
  public int i;
  public int j;
  public int h; // heightMap[i][j] or the height after filling water
  public T(int i, int j, int h) {
    this.i = i;
    this.j = j;
    this.h = h;
  }
}

class Solution {
  public int trapRainWater(int[][] heightMap) {
    final int m = heightMap.length;
    final int n = heightMap[0].length;
    final int[] dirs = {0, 1, 0, -1, 0};
    int ans = 0;
    PriorityQueue<T> pq = new PriorityQueue<>((a, b) -> a.h - b.h);
    boolean[][] seen = new boolean[m][n];

    for (int i = 0; i < m; ++i) {
      pq.offer(new T(i, 0, heightMap[i][0]));
      pq.offer(new T(i, n - 1, heightMap[i][n - 1]));
      seen[i][0] = true;
      seen[i][n - 1] = true;
    }

    for (int j = 1; j < n - 1; ++j) {
      pq.offer(new T(0, j, heightMap[0][j]));
      pq.offer(new T(m - 1, j, heightMap[m - 1][j]));
      seen[0][j] = true;
      seen[m - 1][j] = true;
    }

    while (!pq.isEmpty()) {
      final int i = pq.peek().i;
      final int j = pq.peek().j;
      final int h = pq.poll().h;
      for (int k = 0; k < 4; ++k) {
        final int x = i + dirs[k];
        final int y = j + dirs[k + 1];
        if (x < 0 || x == m || y < 0 || y == n)
          continue;
        if (seen[x][y])
          continue;
        if (heightMap[x][y] < h) {
          ans += h - heightMap[x][y];
          pq.offer(new T(x, y, h)); // fill the water on grid[x][y]
        } else {
          pq.offer(new T(x, y, heightMap[x][y]));
        }
        seen[x][y] = true;
      }
    }

    return ans;
  }
}

class T {
  public int i;
  public int j;
  public int d; // max difference of (i, j) and its neighbors
  public T(int i, int j, int d) {
    this.i = i;
    this.j = j;
    this.d = d;
  }
}

class Solution {
  public int minimumEffortPath(int[][] heights) {
    final int m = heights.length;
    final int n = heights[0].length;
    final int[] dirs = {0, 1, 0, -1, 0};
    // dist[i][j] := max absolute difference to reach (i, j)
    int[][] diff = new int[m][n];
    boolean[][] seen = new boolean[m][n];
    PriorityQueue<T> pq = new PriorityQueue<>((a, b) -> a.d - b.d);

    Arrays.stream(diff).forEach(row -> Arrays.fill(row, Integer.MAX_VALUE));
    diff[0][0] = 0;

    pq.offer(new T(0, 0, diff[0][0]));

    while (!pq.isEmpty()) {
      final int i = pq.peek().i;
      final int j = pq.peek().j;
      final int d = pq.poll().d;
      if (i == m - 1 && j == n - 1)
        return d;
      seen[i][j] = true;
      for (int k = 0; k < 4; ++k) {
        final int x = i + dirs[k];
        final int y = j + dirs[k + 1];
        if (x < 0 || x == m || y < 0 || y == n)
          continue;
        if (seen[x][y])
          continue;
        final int newDiff = Math.abs(heights[i][j] - heights[x][y]);
        final int maxDiff = Math.max(diff[i][j], newDiff);
        if (diff[x][y] > maxDiff) {
          diff[x][y] = maxDiff;
          pq.offer(new T(x, y, maxDiff));
        }
      }
    }

    throw new IllegalArgumentException();
  }
}

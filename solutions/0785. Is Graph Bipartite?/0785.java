enum Color { WHITE, RED, GREEN }

class Solution {
  public boolean isBipartite(int[][] graph) {
    Color[] colors = new Color[graph.length];
    Arrays.fill(colors, Color.WHITE);

    for (int i = 0; i < graph.length; ++i) {
      // already colored, do nothing
      if (colors[i] != Color.WHITE)
        continue;
      // colors[i] == Color.WHITE
      colors[i] = Color.RED; // always paint w/ Color.RED
      // BFS
      Queue<Integer> q = new LinkedList<>(Arrays.asList(i));
      while (!q.isEmpty()) {
        for (int size = q.size(); size > 0; --size) {
          final int u = q.poll();
          for (final int v : graph[u]) {
            if (colors[v] == colors[u])
              return false;
            if (colors[v] == Color.WHITE) {
              colors[v] = colors[u] == Color.RED ? Color.GREEN : Color.RED;
              q.offer(v);
            }
          }
        }
      }
    }

    return true;
  }
}

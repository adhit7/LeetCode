class T {
  public int u;
  public int dist;
  public int stops;
  public T(int u, int dist, int stops) {
    this.u = u;
    this.dist = dist;
    this.stops = stops;
  }
}

class Solution {
  public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
    List<int[]>[] graph = new List[n];
    // (u, dist, stops): min-heap sorted by dist
    PriorityQueue<T> pq = new PriorityQueue<>((a, b) -> a.dist - b.dist);
    int[][] minDist = new int[n][k + 2];

    for (int i = 0; i < graph.length; ++i)
      graph[i] = new ArrayList<>();

    for (int[] f : flights)
      graph[f[0]].add(new int[] {f[1], f[2]});

    pq.offer(new T(src, 0, k + 1)); // start with node src with dist == 0
    Arrays.stream(minDist).forEach(A -> Arrays.fill(A, Integer.MAX_VALUE));
    minDist[src][k + 1] = 0;

    while (!pq.isEmpty()) {
      final int u = pq.peek().u;
      final int dist = pq.peek().dist;
      final int stops = pq.poll().stops;
      if (u == dst)
        return dist;
      if (stops > 0)
        for (int[] nodes : graph[u]) {
          final int v = nodes[0];
          final int w = nodes[1];
          final int newDist = dist + w;
          if (newDist < minDist[v][stops - 1]) {
            minDist[v][stops - 1] = newDist;
            pq.offer(new T(v, dist + w, stops - 1));
          }
        }
    }

    return -1;
  }
}

class T {
  public int u;
  public int dist;
  public int d; // remaining discounts
  public T(int u, int dist, int d) {
    this.u = u;
    this.dist = dist;
    this.d = d;
  }
}

class Solution {
  public int minimumCost(int n, int[][] highways, int discounts) {
    List<Pair<Integer, Integer>>[] graph = new List[n];
    PriorityQueue<T> pq = new PriorityQueue<>((a, b) -> a.dist - b.dist);
    Map<Integer, Integer> minDiscounts = new HashMap<>();

    for (int i = 0; i < graph.length; i++)
      graph[i] = new ArrayList<>();

    for (int[] h : highways) {
      final int city1 = h[0];
      final int city2 = h[1];
      final int toll = h[2];
      graph[city1].add(new Pair<>(city2, toll));
      graph[city2].add(new Pair<>(city1, toll));
    }

    pq.offer(new T(0, 0, discounts));

    while (!pq.isEmpty()) {
      final int u = pq.peek().u;
      final int dist = pq.peek().dist;
      final int d = pq.poll().d;
      if (u == n - 1)
        return dist;
      if (minDiscounts.getOrDefault(u, -1) >= d)
        continue;
      minDiscounts.put(u, d);
      for (var pair : graph[u]) {
        final int v = pair.getKey();
        final int w = pair.getValue();
        pq.offer(new T(v, dist + w, d));
        if (d > 0)
          pq.offer(new T(v, dist + w / 2, d - 1));
      }
    }
    return -1;
  }
}

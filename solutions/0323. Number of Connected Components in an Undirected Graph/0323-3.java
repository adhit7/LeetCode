class UF {
  public UF(int n) {
    size = n;
    id = new int[n];
    for (int i = 0; i < n; ++i)
      id[i] = i;
  }

  public void union(int u, int v) {
    final int i = find(u);
    final int j = find(v);
    if (i == j)
      return;
    id[i] = j;
    --size;
  }

  public int getSize() {
    return size;
  }

  private int size;
  private int[] id;

  private int find(int u) {
    return id[u] == u ? u : (id[u] = find(id[u]));
  }
}

class Solution {
  public int countComponents(int n, int[][] edges) {
    UF uf = new UF(n);

    for (int[] edge : edges)
      uf.union(edge[0], edge[1]);

    return uf.getSize();
  }
}

class UF {
 public:
  UF(int n) : id(n) {
    iota(begin(id), end(id), 0);
  }

  bool union_(int u, int v) {
    const int i = find(u);
    const int j = find(v);
    if (i == j)
      return false;
    id[i] = j;
    return true;
  }

 private:
  vector<int> id;

  int find(int u) {
    return id[u] == u ? u : id[u] = find(id[u]);
  }
};

class Solution {
 public:
  vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    UF uf(edges.size() + 1);

    for (const auto& edge : edges)
      if (!uf.union_(edge[0], edge[1]))
        return edge;

    throw;
  }
};

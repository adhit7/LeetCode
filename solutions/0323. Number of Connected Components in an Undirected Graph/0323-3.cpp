class UF {
 public:
  UF(int n) : size(n), id(n) {
    iota(begin(id), end(id), 0);
  }

  void union_(int u, int v) {
    const int i = find(u);
    const int j = find(v);
    if (i == j)
      return;
    id[i] = j;
    --size;
  }

  int getSize() {
    return size;
  }

 private:
  int size;
  vector<int> id;

  int find(int u) {
    return id[u] == u ? u : id[u] = find(id[u]);
  }
};

class Solution {
 public:
  int countComponents(int n, vector<vector<int>>& edges) {
    UF uf(n);

    for (const auto& edge : edges)
      uf.union_(edge[0], edge[1]);

    return uf.getSize();
  }
};

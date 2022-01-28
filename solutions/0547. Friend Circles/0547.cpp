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
  int findCircleNum(vector<vector<int>>& M) {
    const int n = M.size();
    UF uf(n);

    for (int i = 0; i < n; ++i)
      for (int j = i; j < n; ++j)
        if (M[i][j] == 1)
          uf.union_(i, j);

    return uf.getSize();
  }
};

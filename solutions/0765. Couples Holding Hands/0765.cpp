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
  int minSwapsCouples(vector<int>& row) {
    const int n = row.size() / 2;
    UF uf(n);

    for (int i = 0; i < n; ++i) {
      const int a = row[2 * i];
      const int b = row[2 * i + 1];
      uf.union_(a / 2, b / 2);
    }

    return n - uf.getSize();
  }
};

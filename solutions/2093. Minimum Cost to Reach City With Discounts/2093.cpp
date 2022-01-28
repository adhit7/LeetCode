struct T {
  int u;
  int dist;
  int d;  // remaining discounts
  T(int u, int dist, int d) : u(u), dist(dist), d(d) {}
};

class Solution {
 public:
  int minimumCost(int n, vector<vector<int>>& highways, int discounts) {
    vector<vector<pair<int, int>>> graph(n);
    auto compare = [](const T& a, const T& b) { return a.dist > b.dist; };
    priority_queue<T, vector<T>, decltype(compare)> pq(compare);
    unordered_map<int, int> minDiscounts;

    for (const auto& h : highways) {
      const int city1 = h[0];
      const int city2 = h[1];
      const int toll = h[2];
      graph[city1].emplace_back(city2, toll);
      graph[city2].emplace_back(city1, toll);
    }

    pq.emplace(0, 0, discounts);

    while (!pq.empty()) {
      const auto [u, dist, d] = pq.top();
      pq.pop();
      if (u == n - 1)
        return dist;
      if (minDiscounts.count(u) && minDiscounts[u] >= d)
        continue;
      minDiscounts[u] = d;
      for (const auto& [v, w] : graph[u]) {
        pq.emplace(v, dist + w, d);
        if (d > 0)
          pq.emplace(v, dist + w / 2, d - 1);
      }
    }

    return -1;
  }
};

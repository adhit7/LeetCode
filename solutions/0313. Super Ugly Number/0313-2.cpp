struct UglyNum {
  int prime;
  int index;   // point to the next index of uglyNums
  long value;  // prime * uglyNums[index]
  UglyNum(int prime, int index, long value)
      : prime(prime), index(index), value(value) {}
};

class Solution {
 public:
  int nthSuperUglyNumber(int n, vector<int>& primes) {
    auto compare = [&](const UglyNum& a, const UglyNum& b) {
      return a.value > b.value;
    };
    priority_queue<UglyNum, vector<UglyNum>, decltype(compare)> pq(compare);
    vector<int> uglyNums{1};

    for (const int prime : primes)
      pq.emplace(prime, 1, prime * uglyNums[0]);

    while (uglyNums.size() < n) {
      uglyNums.push_back(pq.top().value);
      while (pq.top().value == uglyNums.back()) {
        const auto [prime, index, _] = pq.top();
        pq.pop();
        pq.emplace(prime, index + 1, prime * (long)uglyNums[index]);
      }
    }

    return uglyNums.back();
  }
};

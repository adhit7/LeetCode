class Solution {
 public:
  int waysToSplit(vector<int>& nums) {
    constexpr int kMod = 1e9 + 7;
    const int n = nums.size();
    int ans = 0;
    vector<int> prefix(n);

    partial_sum(begin(nums), end(nums), begin(prefix));

    for (int i = 0, j = 0, k = 0; i < n - 2; ++i) {
      // find first index j s.t.
      // left = prefix[i] <= mid = prefix[j] - prefix[i]
      while (j <= i || (j < n - 1 && prefix[i] > prefix[j] - prefix[i]))
        ++j;
      // find first index k s.t.
      // mid = prefix[k] - prefix[i] > right = prefix[-1] - prefix[k]
      while (k < j ||
             (k < n - 1 && prefix[k] - prefix[i] <= prefix.back() - prefix[k]))
        ++k;
      ans = (ans + k - j) % kMod;
    }

    return ans;
  }
};

class Solution {
 public:
  int reversePairs(vector<int>& nums) {
    int ans = 0;
    mergeSort(nums, 0, nums.size() - 1, ans);
    return ans;
  }

 private:
  void mergeSort(vector<int>& nums, int l, int r, int& ans) {
    if (l >= r)
      return;

    const int m = l + (r - l) / 2;
    mergeSort(nums, l, m, ans);
    mergeSort(nums, m + 1, r, ans);
    merge(nums, l, m, r, ans);
  }

  void merge(vector<int>& nums, int l, int m, int r, int& ans) {
    const int lo = m + 1;
    int hi = m + 1;  // 1st index s.t. nums[i] <= 2 * nums[lo]

    // for each index i in range [l, m], add hi - lo to ans
    for (int i = l; i <= m; ++i) {
      while (hi <= r && nums[i] > (long)2 * nums[hi])
        ++hi;
      ans += hi - lo;
    }

    vector<int> sorted(r - l + 1);
    int k = 0;      // sorted's index
    int i = l;      // left's index
    int j = m + 1;  // right's index

    while (i <= m && j <= r)
      if (nums[i] < nums[j])
        sorted[k++] = nums[i++];
      else
        sorted[k++] = nums[j++];

    // put possible remaining left part to the sorted array
    while (i <= m)
      sorted[k++] = nums[i++];

    // put possible remaining right part to the sorted array
    while (j <= r)
      sorted[k++] = nums[j++];

    copy(begin(sorted), end(sorted), begin(nums) + l);
  }
};

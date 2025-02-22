class Solution {
  public int waysToSplit(int[] nums) {
    final int kMod = (int) 1e9 + 7;
    final int n = nums.length;
    int ans = 0;
    int[] prefix = nums.clone();

    for (int i = 1; i < n; ++i)
      prefix[i] += prefix[i - 1];

    for (int i = 0, j = 0, k = 0; i < n - 2; ++i) {
      // find first index j s.t.
      // left = prefix[i] <= mid = prefix[j] - prefix[i]
      while (j <= i || (j < n - 1 && prefix[i] > prefix[j] - prefix[i]))
        ++j;
      // find first index k s.t.
      // mid = prefix[k] - prefix[i] > right = prefix[-1] - prefix[k]
      while (k < j || (k < n - 1 && prefix[k] - prefix[i] <= prefix[prefix.length - 1] - prefix[k]))
        ++k;
      ans = (ans + k - j) % kMod;
    }

    return ans;
  }
}

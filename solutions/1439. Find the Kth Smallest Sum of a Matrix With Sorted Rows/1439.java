class T {
  public int i;
  public int j;
  public int sum; // nums1[i] + nums2[j]
  public T(int i, int j, int sum) {
    this.i = i;
    this.j = j;
    this.sum = sum;
  }
}

class Solution {
  public int kthSmallest(int[][] mat, int k) {
    int[] row = mat[0];

    for (int i = 1; i < mat.length; ++i)
      row = kSmallestPairSums(row, mat[i], k);

    return row[k - 1];
  }

  // very similar to 373. Find K Pairs with Smallest Sums
  private int[] kSmallestPairSums(int[] nums1, int[] nums2, int k) {
    List<Integer> ans = new ArrayList<>();
    PriorityQueue<T> pq = new PriorityQueue<>((a, b) -> a.sum - b.sum);

    for (int i = 0; i < k && i < nums1.length; ++i)
      pq.offer(new T(i, 0, nums1[i] + nums2[0]));

    while (!pq.isEmpty() && ans.size() < k) {
      final int i = pq.peek().i;
      final int j = pq.poll().j;
      ans.add(nums1[i] + nums2[j]);
      if (j + 1 < nums2.length)
        pq.offer(new T(i, j + 1, nums1[i] + nums2[j + 1]));
    }

    return ans.stream().mapToInt(i -> i).toArray();
  }
}

class Solution {
  public int sumSubarrayMins(int[] A) {
    final int kMod = (int) 1e9 + 7;
    final int n = A.length;
    long ans = 0;
    int[] prev = new int[n];
    int[] next = new int[n];
    Stack<Integer> stack = new Stack<>();

    Arrays.fill(prev, -1);
    Arrays.fill(next, n);

    for (int i = 0; i < A.length; ++i) {
      while (!stack.isEmpty() && A[stack.peek()] > A[i]) {
        final int index = stack.pop();
        next[index] = i;
      }
      if (!stack.isEmpty())
        prev[i] = stack.peek();
      stack.add(i);
    }

    for (int i = 0; i < A.length; ++i)
      ans = (ans + (long) A[i] * (i - prev[i]) * (next[i] - i)) % kMod;

    return (int) ans;
  }
}

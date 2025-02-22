class Solution {
  public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
    List<TreeNode> ans = new ArrayList<>();
    Set<Integer> toDeleteSet = new HashSet<>();

    for (final int val : to_delete)
      toDeleteSet.add(val);

    dfs(root, toDeleteSet, true, ans);
    return ans;
  }

  private TreeNode dfs(TreeNode root, Set<Integer> toDeleteSet, boolean isRoot,
                       List<TreeNode> ans) {
    if (root == null)
      return null;

    final boolean deleted = toDeleteSet.contains(root.val);
    if (isRoot && !deleted)
      ans.add(root);

    // if root is deleted, both children have the possibility to be a new root
    root.left = dfs(root.left, toDeleteSet, deleted, ans);
    root.right = dfs(root.right, toDeleteSet, deleted, ans);
    return deleted ? null : root;
  }
}

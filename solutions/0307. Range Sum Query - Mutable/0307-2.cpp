struct SegmentTreeNode {
  int lo;
  int hi;
  int sum;
  SegmentTreeNode* left;
  SegmentTreeNode* right;
  SegmentTreeNode(int lo, int hi, int sum, SegmentTreeNode* left = nullptr,
                  SegmentTreeNode* right = nullptr)
      : lo(lo), hi(hi), sum(sum), left(left), right(right) {}
  ~SegmentTreeNode() {
    delete left;
    delete right;
    left = nullptr;
    right = nullptr;
  }
};

class SegmentTree {
 public:
  SegmentTree(const vector<int>& nums) : nums(move(nums)) {
    root.reset(build(0, nums.size() - 1));
  }

  std::unique_ptr<SegmentTreeNode> root;

  void update(SegmentTreeNode* root, int i, int val) {
    if (root->lo == i && root->hi == i) {
      root->sum = val;
      return;
    }
    const int mid = (root->lo + root->hi) / 2;
    if (i <= mid)
      update(root->left, i, val);
    else
      update(root->right, i, val);
    root->sum = root->left->sum + root->right->sum;
  }

  int sumRange(SegmentTreeNode* root, int i, int j) const {
    if (root->lo == i && root->hi == j)
      return root->sum;
    const int mid = (root->lo + root->hi) / 2;
    if (j <= mid)
      return sumRange(root->left, i, j);
    if (i > mid)
      return sumRange(root->right, i, j);
    return sumRange(root->left, i, mid) + sumRange(root->right, mid + 1, j);
  }

 private:
  const vector<int> nums;

  SegmentTreeNode* build(int lo, int hi) const {
    if (lo == hi)
      return new SegmentTreeNode(lo, hi, nums[lo]);
    const int mid = (lo + hi) / 2;
    auto left = build(lo, mid);
    auto right = build(mid + 1, hi);
    return new SegmentTreeNode(lo, hi, left->sum + right->sum, left, right);
  }
};

class NumArray {
 public:
  NumArray(vector<int>& nums) : tree(nums) {}

  void update(int index, int val) {
    tree.update(tree.root.get(), index, val);
  }

  int sumRange(int left, int right) {
    return tree.sumRange(tree.root.get(), left, right);
  }

 private:
  SegmentTree tree;
};

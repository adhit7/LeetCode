class TrieNode:
  def __init__(self):
    self.children: Dict[str, TrieNode] = defaultdict(TrieNode)
    self.word: Optional[str] = None


class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    m = len(board)
    n = len(board[0])

    ans = []
    root = TrieNode()

    def insert(word: str) -> None:
      node = root
      for c in word:
        if c not in node.children:
          node.children[c] = TrieNode()
        node = node.children[c]
      node.word = word

    for word in words:
      insert(word)

    def dfs(i: int, j: int, node: TrieNode) -> bool:
      if i < 0 or i == m or j < 0 or j == n:
        return False
      if board[i][j] == '*':
        return False

      c = board[i][j]
      if c not in node.children:
        return
      nextNode = node.children[c]
      if nextNode.word:
        ans.append(nextNode.word)
        nextNode.word = None  # prevent duplication

      board[i][j] = '*'
      dfs(i + 1, j, nextNode)
      dfs(i - 1, j, nextNode)
      dfs(i, j + 1, nextNode)
      dfs(i, j - 1, nextNode)
      board[i][j] = c

    for i in range(m):
      for j in range(n):
        dfs(i, j, root)

    return ans

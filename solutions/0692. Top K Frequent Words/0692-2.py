class T:
  def __init__(self, word: str, freq: int):
    self.word = word
    self.freq = freq

  def __lt__(self, other):
    if self.freq == other.freq:
      # words w/ higher frequency and lower alphabetical order are in the bottom
      # of the heap, because we'll pop words w/ lower frequency and higher
      # alphabetical order if the heap's size > k
      return self.word > other.word
    return self.freq < other.freq


class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    ans = []
    pq = []  # max-heap sorted by freq then alphabet

    for word, freq in Counter(words).items():
      heapq.heappush(pq, T(word, freq))
      if len(pq) > k:
        heapq.heappop(pq)

    while pq:
      ans.append(heapq.heappop(pq).word)

    return ans[::-1]

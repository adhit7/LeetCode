class Solution:
  def hIndex(self, citations: List[int]) -> int:
    n = len(citations)

    accumulate = 0
    count = [0] * (n + 1)

    for citation in citations:
      count[min(citation, n)] += 1

    # to find the largeset h-index, loop from back to front
    # i is the candidate h-index
    for i in range(n, -1, -1):
      accumulate += count[i]
      if accumulate >= i:
        return i

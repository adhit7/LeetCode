class Solution:
  def calculate(self, s: str) -> int:
    nums = []  # store nums
    ops = []  # store operators and parentheses

    def calculate(op: chr, b: int, a: int) -> int:
      if op == '+':
        return a + b
      if op == '-':
        return a - b
      if op == '*':
        return a * b
      if op == '/':
        return int(float(a) / b)

    # return True if op1 is a operator and priority(op1) >= priority(op2)
    def precede(op1: chr, op2: chr) -> bool:
      if op1 in ('(', ')'):
        return False
      return op1 in ('*', '/') or op2 in ('+', '-')

    i = 0
    while i < len(s):
      c = s[i]
      if c.isdigit():
        num = ord(c) - ord('0')
        while i + 1 < len(s) and s[i + 1].isdigit():
          num = num * 10 + (ord(s[i + 1]) - ord('0'))
          i += 1
        nums.append(num)
      elif c == '(':
        ops.append(c)
      elif c == ')':
        while ops[-1] != '(':
          nums.append(calculate(ops.pop(), nums.pop(), nums.pop()))
        ops.pop()  # remove '('
      elif c in ('+', '-', '*', '/'):
        while ops and precede(ops[-1], c):
          nums.append(calculate(ops.pop(), nums.pop(), nums.pop()))
        ops.append(c)
      i += 1

    while ops:
      nums.append(calculate(ops.pop(), nums.pop(), nums.pop()))

    return nums[-1]

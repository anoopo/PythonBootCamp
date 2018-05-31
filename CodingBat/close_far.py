"""Given three ints, a b c, return True if one of b or c is "close"
(differing from a by at most 1), while the other is "far",
differing from both other values by 2 or more. Note: abs(num)
computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True"""
def close_far(a, b, c):
  diffBA = abs(b - a)
  diffCB = abs(c - b)
  diffCA = abs(c - a)
  nearCount = 0
  farCount = 0
  for n in (diffBA,diffCB,diffCA):
      if n <= 1:
          nearCount += 1
      else:
          farCount += 1
  return nearCount == 1 and farCount == 2

print (close_far(1, 2, 10))

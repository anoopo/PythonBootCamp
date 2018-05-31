def lone_sum(a, b, c):
  sum = 0
  if a == b == c:
      print (2)
      return 0
  elif a == b and a != c:
      print (3)
      return c
  elif a == c and a != b:
      print (4)
      return b
  elif b == c and b != a:
          print (5)
          return a
  else:
      return a+b+c

print (lone_sum(3,2,3))

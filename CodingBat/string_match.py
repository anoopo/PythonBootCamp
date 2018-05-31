"""
Given 2 strings, a and b, return the number of the positions where they contain
 the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
 since the "xx", "aa", and "az" substrings appear in the same place in
  both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0"""

def string_match(a, b):
  lista = []
  listb = []
  count = 0
  for i in range(len(a)-1):
    lista.append(a[i:i+2])
  for j in range(len(b)-1):
    listb.append(b[j:j+2])
  for i,j in zip(lista,listb):
    if i == j:
      count +=1

  return count

print (string_match('xxcaazz', 'xxbaaz'))

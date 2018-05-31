"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'"""

def not_string(str):
  new_list = str.split()
  if new_list[0] == "not":
    print (str)
  else:
    print ("not " + str)

not_string("not candy")

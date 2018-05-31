"""
Return True if the given string contains an appearance of "xyz" where the xyz
is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""
def xyz_there(str):
  found = False
  if str.startswith("xyz"):
    return True
  else:
    print (str)
    for i in range(1,len(str)-2):
        print (str[i])
        if (str[i:i+3] == "xyz"):
            found = True
            return (str[i-1] != ".")
    return found

print (xyz_there('abcxyz'))

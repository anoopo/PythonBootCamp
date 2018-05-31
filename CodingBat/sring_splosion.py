def string_splosion(str):
  result = ""
  for i in range(len(str)):
      print (i)
      result = result + str[:i+1]
      print (result)
  return result + str

print (string_splosion("Code"))
str = "anoop"
print (str[-2:])

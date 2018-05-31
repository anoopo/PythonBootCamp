"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True"""
def array123(nums):
  sequence = [1,2,3]
  found = False
  for i in range(len(nums)-2):
      list = [nums[i],nums[i+1],nums[i+2]]
      print (list)
      if list == sequence:
          found = True
          break
   return found
print (array123([1, 1, 2, 4, 1]))

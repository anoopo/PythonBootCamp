"""
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that
 come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6"""
def sum13(nums):
  if len(nums) == 0:
    return 0
  else:
    while nums.count(13) > 0:
      print ("inside while")
      index13 = nums.index(13)
      if index13 < len(nums)-1:
        del nums[index13+1]
      del nums[index13]
    return sum(nums)

print (sum13([1, 2, 2, 1, 13]))

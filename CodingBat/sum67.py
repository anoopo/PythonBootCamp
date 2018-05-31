"""
Return the sum of the numbers in the array, except ignore sections of
numbers starting with a 6 and extending to the next 7
(every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""
def sum67(nums):
  while nums.count(6) > 0 and nums.count(7) > 0:
    index6 = nums.index(6)
    index7 = nums.index(7,index6)
    if index7 == len(nums)-1:
        del nums[index6:]
    else:
        del nums[index6:index7+1]
  return sum(nums)


print (sum67([2, 7, 6, 2, 6, 7, 2, 7]))

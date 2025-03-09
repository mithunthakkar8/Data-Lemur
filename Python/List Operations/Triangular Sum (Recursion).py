def triangular_sum(nums):
  newNums = [None]*(len(nums)-1)
  if len(nums)==1:
    return nums[0]
  for i in range(0,len(nums)):
    if i+1<len(nums):
      newNums[i] = (nums[i] + nums[i+1])%10
  return triangular_sum(newNums)
  

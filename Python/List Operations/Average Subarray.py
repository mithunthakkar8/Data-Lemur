import numpy as np
def max_avg_subarray(nums, k):
    if len(nums)<=k:
        return round(np.mean(nums),2)
    
    max_sub = np.mean(nums[0:k])
    for i in range(len(nums)-2):
        if np.mean(nums[i:i+k])>max_sub:
            max_sub = np.mean(nums[i:i+k])
    return round(max_sub,2)

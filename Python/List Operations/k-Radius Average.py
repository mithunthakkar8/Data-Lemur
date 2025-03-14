import numpy as np  

def k_radius_avg(nums, k):
    # If the list is too short to compute any k-radius average, return a list filled with -1
    if len(nums) <= 2 * k:
        return [-1] * len(nums)

    # Initialize an empty list to store the computed k-radius averages
    averages = []

    # Iterate through the list, considering only indices where a full k-radius subarray exists
    for i in range(k, len(nums) - k):
        # Extract the subarray centered at index i with radius k
        subarray = nums[i - k:i + k + 1]
        
        # Compute the mean of the subarray and round it to 2 decimal places
        avg = round(np.mean(subarray), 2)
        
        # Append the computed average to the list
        averages.append(avg)

    # Pad the computed averages with -1 on both sides to match the original list length
    padded_avgs = np.pad(averages, (k, k), mode='constant', constant_values=-1)

    # Convert the padded NumPy array back to a Python list and return the result
    return list(padded_avgs)

# Problem: Maximum Subarray 
# Approach: Kadane's Algo
# Time: O(n)
# Space: O(1)

def maximumSubarray(nums:list):
    maximum = nums[0]
    curr  = nums[0]
    
    for i in range(1, len(nums)):
        if curr < 0:
            curr = nums[i]
        else:
            curr += nums[i]
            
        maximum = max(maximum, curr)

    return maximum
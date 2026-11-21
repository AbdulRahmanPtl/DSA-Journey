# Problem: Missing Number
# Approach: Linear & total sum - array sum
# Time: O(n)
# Space: O(1)

def missingNumber(nums:list):
    n = len(nums)
    
    total_sum = n * (n+1) // 2
    
    arr_result = 0
    
    for item in nums:
        arr_result += item
        
    return total_sum - arr_result
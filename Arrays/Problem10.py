# Problem: Longest Subarray with Sum K (+ve /-ve)
# Approach: Prefix Sum
# Time: O(n)
# Space: O(n)

nums = [0, 1, -1, 2]
k = 2

def longestSubarraySum(nums:list, k:int):
    prefix = 0
    longest = 0
    hashmap = {0:-1}
    
    for i in range(len(nums)):
        prefix += nums[i]
        
        need = prefix - k
        
        if need in hashmap:
            longest = max(longest, i - hashmap[need])
        
        if prefix not in hashmap:
            hashmap[prefix] = i
        
    return longest
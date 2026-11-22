from collections import Counter
# Problem: 2 Sum
# Approach: Hashmap
# Time: O(n)
# Space: O(1)

# LeetCode
def twoSum(nums:list, target:int):
    hashmap = {}
    
    for i in range(len(nums)):
        needed = target - nums[i]
        
        if needed in hashmap:
            return [hashmap[needed], i]
        hashmap[nums[i]] = i
        

# GeeksForGeeks
def allPairsWithSum(nums1:list, nums2:list, target:int):
    if not nums1 or not nums2:
        return []
    
    nums2 = Counter(nums2)
    result = []
    
    for item in nums1:
        need = target - item
        
        if need in nums2:
            result += [[item, need]] * nums2[need]
            
    return sorted(result)
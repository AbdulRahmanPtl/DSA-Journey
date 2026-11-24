# Problem: Rearrange array elements by sign
# Approach: Two Pointers
# Time: O(n)
# Space: O(1) Auxilary Space

# LeetCode
def rearrangeArray(nums:list):
    n = len(nums)
    result = [0]*n
    even,odd=0,1
    
    for item in nums:
        if item > 0:
            result[even] = item
            even+=2
        else:
            result[odd] = item
            odd+=2
    return result

# GeeksForGeeks
# Two bucket + Two Pointers 
# Time: O(n)
# Space: O(n)
def rearrange(nums:list):
    positive =[]
    negative =[]
    result = []
    for item in nums:
        if item >= 0:
            positive.append(item)
        else:
            negative.append(item)
    
    i = j = 0
    while i < len(positive) and j < len(negative):
        result.append(positive[i])
        result.append(negative[j])
        i+=1
        j+=1
        
    while i < len(positive):
        result.append(positive[i])
        i+=1
    
    while j < len(negative):
        result.append(negative[j])
        j+=1
        
    return result
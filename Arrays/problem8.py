# Problem: max Consicutive Once
# Approach: Linear
# Time: O(n)
# Space: O(1)

def maxConsicutiveOnce(nums:list):
    left = 0
    max_count = 0
    count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            left = right + 1
            count = 0
        else:
            count+=1
            max_count = count if count > max_count else max_count
            
    return max_count

print(maxConsicutiveOnce(nums))
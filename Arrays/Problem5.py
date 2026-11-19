# Problem: Rotate Array by K steps
# Approach: Reversal
# Time: O(n)
# Space: O(1)

def reverse(nums: list, left:int, right:int):
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1

def rotateArray(nums:list, k:int):
    n = len(nums)
    
    k = k % n
    if k == 0:
        return nums
            
    # reversing complete array
    reverse(nums, 0, n-1)
    # resvering the starting k elements
    reverse(nums, 0, k-1)
    # # reversing from k to n
    reverse(nums, k, n-1)
    
    return nums
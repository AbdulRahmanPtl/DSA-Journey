# Problem: Sort Colors
# Approach: 2 Pointers
# Time: O(n)
# Space: O(1)

# nums = [2, 0, 2, 1, 1, 0]
nums = [2, 0, 1]

def sortColors(nums:list):
    low = mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low+=1
            mid += 1
            
        elif nums[mid] == 2:
            nums[mid],nums[high] = nums[high],nums[mid]
            high-=1
        
        else:
            mid += 1
        
    return nums

print(sortColors(nums))
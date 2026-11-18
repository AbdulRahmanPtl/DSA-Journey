# Problem: Check Array is Sorted
# Approach: Linear
# Time: O(n)
# Space: O(1)

# Approach - 1
def checkArraySorted(nums:list):
    mark = -1
    if len(nums) < 2:
        return True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            mark = i  
            break
        
    if mark != -1:
        for j in range(mark+1, len(nums)):
            if nums[j] < nums[j-1]:
                return False
            
    return True if nums[0] > nums[-1] or mark == -1 else False
    
# Approach - 2
def checkArraySorted(nums:list)
    count = 0
    n = len(nums)
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
        if count > 1:
            return False
    
    return True

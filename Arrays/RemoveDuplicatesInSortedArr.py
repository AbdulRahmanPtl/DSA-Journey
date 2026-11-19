# Problem: Remove Duplicates From Sorted Array
# Approach: read , write pointer
# Time: O(n)
# Space: O(1)


def RemoveDuplicates(nums:list):
    write = 0
    for read in range(1, len(nums)):
        if nums[write] != nums[read]:
            write+=1
            nums[write] = nums[read]
        
    return write+1
# Problem: Moves Zeros
# Approach: Read , Write Pointers
# Time: O(n)
# Space: O(1)

def moveZeros(nums:list):
    write = 0
    
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[read],nums[write] = nums[write],nums[read]
            write +=1

print(moveZeros(nums))
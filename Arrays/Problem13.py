# Problem: Majority Element
# Approach: Linear
# Time: O(n)
# Space: O(1)

# Leetcode
def majorityElement(nums:list):
    count = 0
    element = 0
    
    for item in nums:
        # initally or when count becomes zero assingn new element
        if count == 0:
            element = item
            count += 1
            
        # if element is different decrease count
        elif item != element:
            count-=1
        else:
            count+=1
            
    return element
            
# GeeksForGeeks
# Appraoch: Hashmap
# Time: O(n)
# Space: O(n) (Auxilary Space)
def majorityElement(nums:list):
    hashmap = {}
    
    for item in nums:
        hashamp[item] = hashmap.get(item, 0)+1
        
    for k,v in hashmap.items():
        if v > len(nums) // 2:
            return k
    
    return -1
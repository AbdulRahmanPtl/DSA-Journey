# Problem: Union Of 2 Sorted Array
# Approach: Two Pointers 
# Time: O(n)
# Space: O(1) Auxilary Space
        
def unionOf2SortedArray(nums1:list, nums2:list):
    i = 0
    j = 0

    result = []
    
    result.append(min(nums1[i], nums2[j]))
    
    while i < len(nums1) and j < len(nums2):
        
        if nums1[i] < nums2[j]:
            if result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
        
        elif nums2[j] < nums1[i]:
            if result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1
            
        else:
            if result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
            j+=1
            
    while i < len(nums1):
        if result[-1] != nums1[i]:
            result.append(nums1[i])
        i+=1
        
    while j < len(nums2):
        if result[-1] != nums2[j]:
            result.append(nums2[j])
        j+=1
        
    return result
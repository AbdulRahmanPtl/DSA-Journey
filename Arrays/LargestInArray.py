# problem: Largest In Array
# Approach: Linear Search
# Time: O(n)
# Space: O(1)

def LargestInArray(arr:list):
    maximum = arr[0]
    
    for i in range(1, len(arr)):
        maximum = arr[i] if arr[i] > maximum else maximum
        
    return maximum
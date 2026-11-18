# Problem: Second Largest
# Appoach: Linear Search
# Time: O(n)
# Space: O(1)

def SecondLargest(arr:list):
    first_max = arr[0]
    second_max = -1
    
    for i in range(1, len(arr)):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
            
        else:
            if arr[i] < first_max and arr[i] > second_max:
                second_max = arr[i]
    
    return second_max
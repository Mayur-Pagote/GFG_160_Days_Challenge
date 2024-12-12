#Unable to solve
def circularSubarraySum(arr):
    # Edge case: if the array is empty
    if not arr:
        return 0
    
    n = len(arr)
    
    # Initialize variables
    max_sum = arr[0]  # For max subarray sum (Kadane's result)
    min_sum = arr[0]  # For min subarray sum (Modified Kadane's result)
    total_sum = arr[0]  # To calculate the total sum of the array
    current_max = arr[0]  # To track the current subarray sum for max
    current_min = arr[0]  # To track the current subarray sum for min
    
    # Single pass to calculate max, min subarray sums and total sum
    for i in range(1, n):
        num = arr[i]
        
        # Update total sum
        total_sum += num
        
        # Update max subarray sum
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)
        
        # Update min subarray sum
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)
    
    # If total sum equals the minimum sum, that means all elements are negative
    if total_sum == min_sum:
        return max_sum
    
    # Return the maximum of max subarray sum or the circular sum
    return max(max_sum, total_sum - min_sum)

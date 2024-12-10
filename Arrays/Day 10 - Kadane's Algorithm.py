class Solution:
    def maxSubArraySum(self, arr):
        # Initializing the variables to store the maximum sum found so far
        # and the current sum of the subarray.
        max_sum = arr[0]  # We assume the array has at least one element.
        current_sum = arr[0]
        
        # Iterate through the array starting from the second element
        for num in arr[1:]:
            # Update current_sum: either start a new subarray with the current element or extend the existing one.
            current_sum = max(num, current_sum + num)
            # Update max_sum if we find a larger sum.
            max_sum = max(max_sum, current_sum)
        
        return max_sum

#Time Limit Exceeded
"""
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        res = min(arr)
        length = len(arr)+1
        for i in range (length):
            for j in range (i+1, length):
                if sum(arr[i:j]) > res:
                    res = sum(arr[i:j])
        return res
"""

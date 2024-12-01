class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        # Find the maximum number in the array
        max_num = max(arr)
        
        # Initialize the second maximum to the smallest number in the array
        sec_max = min(arr)
        
        # If the smallest number is equal to the maximum number, it means all elements are the same.
        # Hence, there is no second largest number, so return -1.
        if sec_max == max_num:
            return -1
        
        # Loop through each element in the array
        for i in arr:
            # If the element is greater than the current second maximum
            # and less than the maximum number, update the second maximum.
            if i > sec_max and i < max_num:
                sec_max = i
        
        # Return the second largest number found
        return sec_max

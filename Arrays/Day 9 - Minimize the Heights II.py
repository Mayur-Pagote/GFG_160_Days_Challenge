class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        
        # If there's only one tower, the difference is always 0 after modification
        if n == 1:
            return 0
        
        # Sort the array to make calculation of min and max easier
        arr.sort()
        
        # Initial difference between max and min towers before any operation
        res = arr[-1] - arr[0]
        
        # Loop to calculate the minimum difference
        for i in range(1, n):
            # If we can't decrease arr[i] by k (i.e., it would become negative), skip it
            if arr[i] - k < 0:
                continue

            # Possible new minimum and maximum after modifying elements
            minH = min(arr[0] + k, arr[i] - k)  # new minimum after applying k
            maxH = max(arr[i-1] + k, arr[-1] - k)  # new maximum after applying k
            
            # Store the minimum difference as result
            res = min(res, maxH - minH)
        
        return res

# My approach
"""
class Solution:
    def getMinDiff(self, arr,k):
        res = max(arr) - min(arr)
        l = []
        for i in arr:
            if i-k > 0:
                l.append(i-k)
            else:
                l.append(i+k)
        return min(res,max(l) - min(l))
"""

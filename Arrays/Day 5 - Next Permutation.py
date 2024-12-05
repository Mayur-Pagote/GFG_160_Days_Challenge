# Unable to solve 

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        # Step 1: Find the largest index i such that arr[i] < arr[i + 1]
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i >= 0:
            # Step 2: Find the largest index j such that arr[j] > arr[i]
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            # Step 3: Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
        # Step 4: Reverse the suffix starting at i + 1
        arr[i + 1:] = arr[i + 1:][::-1]

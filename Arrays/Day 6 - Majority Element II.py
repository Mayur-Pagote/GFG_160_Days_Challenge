class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        l = []
        
        # Step 1: Use a dictionary to store frequency of each element
        frequency = {}
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # Step 2: Check if any element appears more than n/3 times
        for num in frequency:
            if frequency[num] > (n / 3):
                l.append(num)
        
        # Step 3: Sort the result list before returning
        return sorted(l)

# Time limit exceeded
"""
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)  # Get the length of the array
        l = []  # List to store the majority elements
        one_third = n / 3  # Calculate one-third of the array length
        arr_set = set(arr)  # Convert the array to a set to remove duplicates
        
        # Loop through each unique element in the array
        for i in arr_set:
            # If the count of element i is greater than one-third of the array length
            if arr.count(i) > one_third:
                l.append(i)  # Add element i to the result list
        
        return l  # Return the list of majority elements
"""

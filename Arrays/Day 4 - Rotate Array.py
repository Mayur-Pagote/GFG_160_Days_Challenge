class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)
        # Normalize d to handle cases where d >= n
        d = d % n
        # Slice the array and rearrange
        arr[:] = arr[d:] + arr[:d]
        return arr

#Time limit exceeded
"""
class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        # Iterate 'd' times to perform d rotations
        for i in range(d):
            # Remove the first element of the array and store it in 'value'
            value = arr.pop(0)
            # Append the removed element to the end of the array
            arr.append(value)
        # Return the rotated array after 'd' rotations
        return arr
"""

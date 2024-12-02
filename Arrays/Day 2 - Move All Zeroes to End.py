class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        # Initialize a pointer for the position to place the non-zero element
        non_zero_index = 0

        # Traverse the array and move non-zero elements forward
        for i in range(n):
            if arr[i] != 0:
                arr[non_zero_index] = arr[i]
                non_zero_index += 1

        # Fill the remaining positions with zeros
        for i in range(non_zero_index, n):
            arr[i] = 0

        return arr

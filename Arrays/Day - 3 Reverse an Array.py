class Solution:
    # Define the method reverseArray that takes a list 'arr' as input
    def reverseArray(self, arr):
        # Reverse the array in place using the reverse() method
        # This modifies the original list directly
        arr.reverse()
        
        # Return the reversed array (which has been modified in place)
        return arr

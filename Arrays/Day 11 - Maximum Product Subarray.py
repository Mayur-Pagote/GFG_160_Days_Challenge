#Unable to solve
class Solution:
    def maxProduct(self, arr):
        # Edge case: if the array is empty, return 0 (though this case may not be given as input).
        if not arr:
            return 0

        # Initialize max_prod, min_prod and the result to the first element of the array.
        max_prod = min_prod = result = arr[0]

        # Iterate through the array starting from the second element.
        for i in range(1, len(arr)):
            # If arr[i] is negative, swap max_prod and min_prod as they can flip when multiplied by negative.
            if arr[i] < 0:
                max_prod, min_prod = min_prod, max_prod

            # Update max_prod and min_prod
            max_prod = max(arr[i], max_prod * arr[i])
            min_prod = min(arr[i], min_prod * arr[i])

            # Update the result with the maximum product found so far.
            result = max(result, max_prod)

        return result

# Unable to solve
from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        # Initialize total profit to 0
        sum_num = 0
        
        # Traverse the prices array from day 1 to the end
        for i in range(1, len(prices)):
            # If current price is greater than the previous day's price
            if prices[i] > prices[i - 1]:
                # Add the profit to the total profit
                sum_num += prices[i] - prices[i - 1]
        
        # Return the total profit
        return sum_num

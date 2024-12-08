class Solution:
    def maximumProfit(self, prices) -> int:
        # Initialize variables
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through the list of prices
        for price in prices:
            # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
            # Calculate the potential profit
            profit = price - min_price
            # Update the maximum profit if the current profit is greater
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

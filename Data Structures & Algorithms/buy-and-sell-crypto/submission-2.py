class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")
        max_profit = 0

        for price in prices:

            # Cheapest buying price
            min_price = min(min_price, price)

            # Profit if we sell today
            profit = price - min_price

            # Best profit so far
            max_profit = max(max_profit, profit)

        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price,price)
            diff= price-min_price
            max_profit=price=max(max_profit,diff)
        return max_profit
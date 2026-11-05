class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = None

        for p in prices:
            current_price = p
            if min_price is None or current_price<min_price:
                min_price = current_price

            current_profit = current_price-min_price
            max_profit = max(max_profit, current_profit)
        
        return max_profit


        
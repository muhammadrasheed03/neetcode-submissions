class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = float("inf")
        best = 0

        for price in prices:
            lowest = min(lowest, price)
            best = max(price-lowest, best)

        return best


        
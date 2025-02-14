class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost=0
        mini=prices[0]
        profit=0
        for i in range(1,len(prices)):
            cost=prices[i]-mini
            profit=max(cost,profit)
            mini=min(prices[i],mini)

        return profit
        # buy_stock=prices[0]
        # current_profit = 0
        # max_profit=0
        # for i in range(len(prices)):
        #     if prices[i] < buy_stock:
        #         buy_stock = prices[i]
            
        #     if prices[i] > buy_stock:
        #         current_profit = prices[i] - buy_stock

        #     if current_profit > max_profit:
        #         max_profit = current_profit
        # return max_profit
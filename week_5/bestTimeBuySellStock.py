
# LeetCode 121. Best Time to Buy and Sell Stock
'''
You are given an array prices where prices[i] is 
the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

'''
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
        """
    left=0
    right=1
    max_profit=0
    
    while right<len(prices):
        
        if prices[right]<prices[left]:
            left=right
        max_profit=max(max_profit,prices[right]-prices[left])
        right+=1
    
    return max_profit
def maxProfit_2(prices):
        
    min_price=float('inf')
    max_profit=0

    for price in prices:
        min_price=min(min_price,price)
        max_profit=max(max_profit,price-min_price)
    return max_profit



if __name__=="__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
    print(maxProfit_2(prices))
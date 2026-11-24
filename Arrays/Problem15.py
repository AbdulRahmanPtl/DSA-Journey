# Problem: Stock Buy and Sell
# Approach: Greedy
# Time: O(n)
# Space: O(1)

# LeetCode
def maxProfit(prices:list):
    buy = prices[0]
    profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        
        elif (prices[i] - buy) > profit:
            profit = prices[i] - buy
            
    return profit

# GeeksForGeeks
def maxProfit(prices:list):
    buy = prices[0]
    profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    
    return profit

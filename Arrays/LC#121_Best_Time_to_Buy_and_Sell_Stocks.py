# ✅ LC#121 Best Time to Buy and Sell Stocks
# 📁 Topic: Arrays / Two Pointers
# 🟢 Difficulty: Easy
# 🧠 Approach: Slinding Window
# 🧑‍💻 Author: Diya Bangad
# 💬 Status: Solved
# 🔗 Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(self, prices):
        l = 0 
        r = 1 
        MaxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                MaxP = max(MaxP,profit)
            else:
                l = r 
            r = r+1
        return MaxP

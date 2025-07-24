# ✅ LC#1 Two Sum
# 📁 Topic: Arrays / Two Pointers
# 🟢 Difficulty: Easy
# 🧠 Approach: Two Pointers
# 🧑‍💻 Author: Diya Bangad
# 💬 Status: Solved
# 🔗 Link: https://leetcode.com/problems/two-sum/

def twoSum(self, nums, target):
        n = len(nums)
        for i in range (n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return (i , j)

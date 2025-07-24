# ✅ LC#35 Search Insert Position
# 📁 Topic: Arrays / Two Pointers
# 🟢 Difficulty: Easy
# 🧠 Approach: Two Pointers
# 🧑‍💻 Author: Diya Bangad
# 💬 Status: Solved
# 🔗 Link: https://leetcode.com/problems/search-insert-position/


def searchInsert(self, nums, target):
        l = 0 
        for r in range(len(nums)):
            if nums[r] == target:
                return r
            else:
                if nums[r] < target:
                    l = l+1
        return l

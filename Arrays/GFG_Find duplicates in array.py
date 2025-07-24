# ✅ GFG Find duplicated in Array
# 📁 Topic: Arrays / Two Pointers
# 🟢 Difficulty: Easy
# 🧠 Approach: Sorting, Two Pointer
# 🧑‍💻 Author: Diya Bangad
# 💬 Status: Solved
# 🔗 Link: https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

def findDuplicates(self, arr):
        # code here
        arr_ans = []
        n = len(arr)
        arr.sort()
        l=0
        for r in range(1,n):
            if arr[l]==arr[r]:
                arr_ans.append(arr[l])
                l=l+1
            else:
                l=l+1
        return arr_ans

# Leetcode Problem: 76. Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard
# Tags: Sliding Window, Hash Table, Two Pointers, String

# ✅ Approach:
# - Use two hash maps:
#   - mapT: character frequency of string t
#   - mapS: current window's frequency in s
# - Slide the window using two pointers (left and right):
#   - Expand right until all required characters are present
#   - Then move left to try minimizing the window while keeping all required characters
# - Track the smallest valid window throughout

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return ""

        # Create mapT: frequency count of characters in t
        mapT = {}
        for ch in t:
            if ch in mapT:
                mapT[ch] += 1
            else:
                mapT[ch] = 1

        required = len(mapT)
        l = 0
        r = 0
        create = 0
        ans = [-1, 0, 0]  # [window length, start, end]

        subStringMap = {}

        while r < len(s):
            c = s[r]
            if c in subStringMap:
                subStringMap[c] += 1
            else:
                subStringMap[c] = 1

            if c in mapT and subStringMap[c] == mapT[c]:
                create += 1

            while l <= r and create == required:
                c = s[l]

                if ans[0] == -1 or ans[0] > r - l + 1:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r

                subStringMap[c] -= 1
                if c in mapT and subStringMap[c] < mapT[c]:
                    create -= 1

                l += 1

            r += 1

        if ans[0] == -1:
            return ""
        else:
            return s[ans[1]:ans[2] + 1]

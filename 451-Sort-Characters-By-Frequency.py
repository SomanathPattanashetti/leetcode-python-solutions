# Leetcode Problem: 451. Sort Characters By Frequency
# Link: https://leetcode.com/problems/sort-characters-by-frequency/
# Difficulty: Medium
# Tags: String, Hash Table, Sorting, Heap (Priority Queue)

# ✅ Approach:
# 1. Count the frequency of each character using a dictionary.
# 2. Sort the dictionary items by frequency in descending order.
# 3. Build the result string by repeating each character based on its frequency.

def sort_freq_wise(s: str) -> str:
    # Step 1: Count frequencies
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 2: Sort by frequency (descending order of counts)
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Build result string
    res = ""
    for ch, count in sorted_chars:
        res += ch * count  # Repeat character 'count' times

    return res


# 🧠 Example:
# Input: s = "tree"
# Step 1: Frequencies -> {'t': 1, 'r': 1, 'e': 2}
# Step 2: Sorted -> [('e', 2), ('t', 1), ('r', 1)]
# Step 3: Build -> "eert" (or "eetr")
# Output: "eert"

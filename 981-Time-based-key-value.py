# LeetCode Problem: 981. Time Based Key-Value Store  
# Link: https://leetcode.com/problems/time-based-key-value-store/  
# Difficulty: Medium  
# Tags: HashMap, Binary Search, Design  

# ✅ Approach:
# We need to build a time-based key-value store. For each key, we can store multiple values along with timestamps.
# - `set(key, value, timestamp)`: stores the key-value pair with the given timestamp.
# - `get(key, timestamp)`: retrieves the value with the **largest timestamp ≤ given timestamp**.
#
# 🔑 Key Observations:
# - We store all (value, timestamp) pairs for a key in a list (in order of timestamp).
# - When querying `get`, we perform a binary search over the timestamps to find the largest timestamp ≤ target.
# - We maintain the sorted order because we always append with increasing timestamps.
# - Binary Search gives efficient O(log n) lookup per key.

class TimeMap:
    def __init__(self):
        # Dictionary to store key -> list of (value, timestamp) tuples
        self.store = {}
        
    def set(self, key, value, timestamp):
        # If key is not present, initialize its list
        if key not in self.store:
            self.store[key] = []
            
        # Append the (value, timestamp) to the list for that key
        self.store[key].append((value, timestamp))
        
    def get(self, key, timestamp):
        # If key does not exist, return empty string
        if key not in self.store:
            return ""
        
        values = self.store[key]
        left = 0
        right = len(values) - 1
        result = ""  # Default to empty if no valid timestamp found
        
        # Binary Search for the largest timestamp <= given timestamp
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]  # Exact match found
            elif values[mid][1] < timestamp:
                result = values[mid][0]  # Possible candidate
                left = mid + 1           # Search right half
            else:
                right = mid - 1          # Search left half
        
        return result  # Return the best candidate found

# 🧠 Example:
# set("foo", "bar", 1)
# get("foo", 1) => "bar" (exact timestamp)
# get("foo", 3) => "bar" (largest timestamp ≤ 3 is 1)

# Operations:
# Time Complexity:
# - set: O(1) since we just append
# - get: O(log n) where n is the number of timestamps for that key (binary search)
# Space Complexity: O(n), storing all values for all keys

# Leetcode Problem: 208. Implement Trie (Prefix Tree)
# Link: https://leetcode.com/problems/implement-trie-prefix-tree/
# Difficulty: Medium
# Tags: Trie, Design, String

# ✅ Approach:
# A Trie (Prefix Tree) is a tree-like data structure used to store words efficiently.
# Each node has:
#   - children: mapping of character -> TrieNode
#   - is_end: boolean flag marking the end of a word
#
# Operations:
# 1. insert(word): Traverse character by character.
#    - If character path doesn’t exist, create a new node.
#    - Move down the path.
#    - Mark the last node as end of the word.
#
# 2. search(word): Use helper (search_prefix).
#    - Check if all characters exist in sequence.
#    - Return True only if final node is marked as word end.
#
# 3. startsWith(prefix): Similar to search, but only checks existence of prefix
#    (no need for is_end to be True).

class TrieNode:
    def __init__(self):
        # Each node has a dictionary mapping characters to children
        self.children = {}
        self.is_end = False

    def contains_key(self, ch):
        return ch in self.children

    def get(self, ch):
        return self.children.get(ch)

    def put(self, ch, node):
        self.children[ch] = node

    def set_end(self):
        self.is_end = True

    def is_end_node(self):
        return self.is_end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def search_prefix(self, word: str) -> TrieNode:
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end_node()

    def starts_with(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None


# 🧠 Example:
# trie = Trie()
# trie.insert("apple")
# trie.search("apple")    # True (word exists)
# trie.search("app")      # False (prefix only, not a full word yet)
# trie.starts_with("app") # True  (prefix exists)
# trie.insert("app")
# trie.search("app")      # True (now "app" is a word)

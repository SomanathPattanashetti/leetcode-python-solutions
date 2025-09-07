# Leetcode Problem: 211. Design Add and Search Words Data Structure
# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Difficulty: Medium
# Tags: Design, Trie, DFS, String

# ✅ Approach:
# Use a Trie (prefix tree) to store words.
# Each node has:
#   - children: a dictionary mapping characters to child nodes
#   - word: a boolean flag marking the end of a word
#
# addWord(word):
#   - Insert each character into the Trie.
#   - Mark the last node as a complete word.
#
# search(word):
#   - Traverse character by character.
#   - If character is '.', try all possible children recursively.
#   - Otherwise, follow the normal path.
#   - Return True if a matching word exists in the Trie.

class TrieNode:
    def __init__(self):
        self.children = {}   # Stores char -> TrieNode
        self.word = False    # Marks the end of a word


class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()   # Root of the Trie

    def addWord(self, word):
        node = self.trie
        for ch in word:
            if ch not in node.children:       # If character not present, create new node
                node.children[ch] = TrieNode()
            node = node.children[ch]          # Move to next character
        node.word = True                      # Mark end of the word

    def searchInNode(self, word, node):
        for i, ch in enumerate(word):
            if ch not in node.children:
                if ch == '.':   # '.' means try all possible children
                    for child in node.children.values():
                        if self.searchInNode(word[i+1:], child):
                            return True
                return False    # Not found
            else:
                node = node.children[ch]  # Move to next character
        return node.word  # Return True if it's end of a word

    def search(self, word):
        return self.searchInNode(word, self.trie)


# 🧠 Example:
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# obj.search("pad") ➝ False  (no "pad" added)
# obj.search("bad") ➝ True   ("bad" exists)
# obj.search(".ad") ➝ True   (matches "bad", "dad", "mad")
# obj.search("b..") ➝ True   (matches "bad")

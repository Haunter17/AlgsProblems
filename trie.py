"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    self.childs = {}
    self.isLeaf = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
    node = self.root
    for ch in word:
      child = node.childs.get(ch)
      if child is None:
        child = TrieNode()
        node.childs[ch] = child
      node = child
    node.isLeaf = True

  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
    node = self.root
    for ch in word:
      child = node.childs.get(ch)
      if child is None:
        return False
      node = child
    return node.isLeaf

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
    node = self.root
    for ch in prefix:
      child = node.childs.get(ch)
      if child is None:
        return False
      node = child
    return True

trie = Trie()
trie.insert('lintcode')
print trie.search('lint')
print trie.search('lintcode')
trie.insert('int')
print trie.startsWith('in')
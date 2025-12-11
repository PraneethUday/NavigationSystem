"""Trie data structure for efficient prefix-based search and autocomplete"""


class TrieNode:
    """A single node in the Trie tree"""

    def __init__(self):
        """Initialize a Trie node"""
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie (prefix tree) data structure for efficient location search and autocomplete.
    Provides O(m) search complexity where m is the length of the search key.
    """

    def __init__(self):
        """Initialize the Trie with a root node"""
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.

        Args:
            word (str): The word to insert
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        """
        Search for all words with the given prefix.

        Args:
            prefix (str): The prefix to search for

        Returns:
            list: List of words matching the prefix (max 5 suggestions)
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.collect_all_words(node, prefix)

    def collect_all_words(self, node, prefix):
        """
        Recursively collect all words from a given node.

        Args:
            node (TrieNode): The node to start from
            prefix (str): The current prefix

        Returns:
            list: List of words (limited to 5 suggestions)
        """
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self.collect_all_words(child_node, prefix + char))
        return words[:5]  # Limit suggestions to 5

    def __repr__(self):
        return "Trie()"

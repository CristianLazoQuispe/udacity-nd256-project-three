import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def suffixes(self, prefix=''):
        """
        Find all of the suffixes for the given node

        :param prefix: string Prepend all suffixes with this prefix, for reasons unclear
        :return: list
        """

        def recurse(nodes, prefix):
            suffixes = []

            for letter, node in nodes.items():
                if node.is_word:
                    suffixes.append(prefix + letter)
                if node.children:
                    suffixes += recurse(node.children, prefix + letter)

            return suffixes

        return recurse(self.children, prefix)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add a word to the trie

        :param word: string
        """
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, letters):
        """
        Retrieve the given sequence of letters in the trie, and return the terminating node

        :param letters: string
        :return: TrieNode|None
        """

        def recurse(node, letters):
            if not letters:
                return node

            head, *tail = letters

            if head not in node.children:
                return None
            return recurse(node.children[head], tail)

        return recurse(self.root, letters)

    def exists(self, word):
        """
        Check if the trie contains a given word

        :param word: string
        :return: bool
        """

        node = self.find(word)
        return False if node is None else node.is_word


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------
word_list = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

autocomplete = Trie()
for word in word_list:
    autocomplete.insert(word)

# Find
assert type(autocomplete.find('ant')) is TrieNode
assert autocomplete.find('zzz') is None

# Exists
assert autocomplete.exists('ant')
assert autocomplete.exists('anthology')
assert not autocomplete.exists('anthony')
assert not autocomplete.exists('an')
assert not autocomplete.exists('zzz')

# Suffixes
node = autocomplete.find('a')
assert node.suffixes() == ['nt', 'nthology', 'ntagonist', 'ntonym']

node = autocomplete.find('ant')
assert node.suffixes('ont') == ['onthology', 'ontagonist', 'ontonym']

node = autocomplete.find('anto')
assert node.suffixes() == ['nym']

node = autocomplete.find('trie')
assert node.suffixes() == []

# Autocomplete with Tries #
Given a "root" node, the solution recursively loops through all of the node's children. Whenever a "word" node is encountered, it is added to the list of suffixes.

## Efficiency ##

### Time efficiency ###
The solution first requires that we locate the "root" node, and then locate all of the node's children. In a worst-case scenario, this means visiting every node in the entire trie.

As such, we can express the time efficiency as `O(n)`, where `n` is the total number of nodes in the tree.

Note that we _cannot_ determine the number of nodes in the tree based on the tree height (i.e. the length of the longest word). That would require a binary tree structure, whereas the solution uses a trie in which each node maybe contain an arbitrary number of child nodes.

### Space efficiency ###
The worst-case scenario is that every single item in the trie is a valid suffix. As such, the space efficiency may also be expressed as `O(n)`, where `n` is the number of nodes in tree.

# Autocomplete with Tries #
Given a "root" node, the solution recursively loops through all of the node's children. Whenever a "word" node is encountered, it is added to the list of suffixes.

## Efficiency ##
### Time efficiency ###
In a worst-case scenario, we need to find every suffix of a single letter, by visiting every node in the entire trie.

In this situation, we can approximate the time efficiency using the length of the longest word in the trie, minus the first character. The represents the longest path from the root of the trie to a leaf node.

Assuming that the longest word in the trie is `n` letters, the worst-case time efficiency is `O(2^(n - 1))`.

For example, given a trie containing the following words, in which the longest word ("anthropology") is 12 letters:

- ant
- anthology
- anthropology
- antipathy

Searching for suffixes of the string "a" would require that we visit `2048` nodes (`2^11`).

### Space efficiency ###
The `suffixes` method does not require any additional space, aside from the list containing the found suffixes.

The worst-case scenario is that every single item in the trie is a valid suffix. As such, the space efficiency may also be expressed as `O(2^(n - 1))`, where `n` is the length of the longest word in the trie.

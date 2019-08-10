# Autocomplete with Tries #
Given a "root" node, the solution recursively loops through all of the node's children. Whenever a "word" node is encountered, it is added to the list of suffixes.

## Efficiency ##

### Time efficiency ###
The solution requires that we first locate the "root" node, representing the prefix string. We then walk the tree below that node (i.e. its children), building a list of the available suffixes.

The worst-case scenario is that the prefix is a single letter, which is the root for every word in the trie, _and_ none of the words share any other letters. For example, the trie contains the words "actor", "all", and "amp", and the prefix is "a".

In this case, we would need to visit every node in the entire trie. The number of nodes in the trie can be determined by multiplying the number of words in the trie (`n`) by the average word length (`l`).

This gives us a time efficiency of `O(nl)`.

### Space efficiency ###
The worst-case scenario when _constructing_ a trie is that none of the words in the trie share a common root. For example, our trie may contain the words "camber", "ogle", and "term".

In this case, the space required by the trie is equal to the number of words the trie contains (`n`), multiplied by the average word length (`l`). This gives us a space efficiency for the trie itself of `O(nl)`.

The `suffixes` method, used to retrieve the suffixes for a given node, uses a list to keep track of the found suffixes. The worst-case scenario is that the prefix is a single letter, which is the root for every word in the trie. For example, the trie contains the words "actor", "all", and "amp", and the prefix is "a".

In this case, the space efficiency for the `suffixes` method would equal the total number of words in the trie, `n`. This gives us a space efficiency for the `suffixes` method of `O(n)`.

It's also worth noting that the `suffixes` method makes uses of recursion, which will require additional space on the call stack.
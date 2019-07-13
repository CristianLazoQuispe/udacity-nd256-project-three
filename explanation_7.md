# HTTPRouter using a Trie #

## Efficiency ##
### Time efficiency ###
The `lookup` method needs to walk the tree in order to find the handler, or determine that there is no handler.

The gives the `lookup` method a time efficiency of `O(n)`, where `n` is the number of segments in the route. For example, the route `/a/b/c/` has `3` segments.

### Space efficiency ###
The space efficiency of the router as a whole is `O(n)`, where `n` is the number of nodes in the trie.

The `lookup` method does not require and additional storage, so its space efficiency is `O(1)`.

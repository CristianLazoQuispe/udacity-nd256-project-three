# HTTPRouter using a Trie #

## Time efficiency ##

### The `lookup` method ###
The `lookup` method needs to walk the tree in order to find the handler, or determine that there is no handler.

This gives the `lookup` method a time efficiency of `O(n)`, where `n` is the number of segments in the route. For example, the route `/a/b/c/` has three segments.

We use the word "segments" rather than "web pages", because it's feasible that a segment may not have an associated handler.

## Space efficiency ##
The space efficiency of the router as a whole is `O(n)`, where `n` is the number of nodes in the trie.

### The `add_handler` method ###
The `add_handler` method splits a given path (`/a/b/c`, for example) into a list of segments (`['a', 'b', 'c']`). This gives the `add_handler` method a space efficiency of `O(n)`, where `n` is the number of segments in the path.

For example, in the following code, `n` is 3:

```python
router = Router()
router.add_handler('/a/b/c', 'Handler')
```

### The `lookup` method ###
As with the `add_handler` method, `lookup` splits the given path into a list of segments. As such the `lookup` also has a space efficiency of `O(n)`, where `n` is the number of segments in the path.

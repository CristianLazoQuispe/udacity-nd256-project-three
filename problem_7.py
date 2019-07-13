import collections


class PageNotFound(Exception):
    pass


class RouteTrieNode(object):
    def __init__(self, handler=None):
        self.children = collections.defaultdict(RouteTrieNode)
        self.handler = handler


class RouteTrie(object):
    def __init__(self, home_handler=None):
        self.root = RouteTrieNode(home_handler)

    def insert(self, path, handler):
        """
        Insert a node at the given path

        :param path: list
        :param handler: string
        """
        current_node = self.root
        for segment in path:
            current_node = current_node.children[segment]
        current_node.handler = handler

    def find(self, path):
        """
        Find the handler for the given path

        :param path: list
        :return: string|None
        """

        def recurse(node, segments):
            if not segments:
                return node

            head, *tail = segments

            if head not in node.children:
                return None
            return recurse(node.children[head], tail)

        node = recurse(self.root, path)
        return node.handler if node is not None else node


class Router(object):
    def __init__(self):
        self.trie = RouteTrie()

    def add_handler(self, path, handler):
        """
        Add a handler for the given route

        :param path: string
        :param handler: string
        """
        self.trie.insert(self._split_path(path), handler)

    def lookup(self, path):
        """
        Return the handler for the given route

        :param path: string
        :return: string|None
        """
        handler = self.trie.find(self._split_path(path))
        if handler is None:
            raise PageNotFound
        return handler

    @classmethod
    def _split_path(cls, path):
        """
        Normalise the path, and split it into segments

        :param path: string
        :return: list
        """
        path = path.strip('/')
        return path.split('/') if path else []


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------
# RouteTrie
trie = RouteTrie('home')
trie.insert(['udacity'], 'udacity')
trie.insert(['udacity', 'courses', 'nd256'], 'data structures and algorithms')

assert trie.root.handler == 'home'
assert trie.root.children['udacity'].handler == 'udacity'
assert trie.root.children['udacity'].children['courses'].handler is None
assert trie.root.children['udacity'].children['courses'].children['nd256'].handler == 'data structures and algorithms'

assert trie.find([]) == 'home'
assert trie.find(['udacity']) == 'udacity'
assert trie.find(['udacity', 'courses']) is None
assert trie.find(['udacity', 'courses', 'nd256']) == 'data structures and algorithms'

# Router
router = Router()

router.add_handler('/', 'home')
router.add_handler('/udacity', 'udacity')

# Add a route with no leading slash, and a trailing slash
router.add_handler('udacity/courses/nd256/', 'data structures and algorithms')

assert router.lookup('/') == 'home'
assert router.lookup('/udacity') == 'udacity'

# Handle leading and trailing slash variants
assert router.lookup('') == 'home'
assert router.lookup('udacity') == 'udacity'
assert router.lookup('udacity/') == 'udacity'

# 404s should raise an exception
try:
    router.lookup('udacity/courses')
    assert False, 'A route without a handler should raise an exception'
except PageNotFound:
    assert True

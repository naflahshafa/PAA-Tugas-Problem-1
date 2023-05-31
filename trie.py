class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def delete(self, word):
        self._delete_helper(self.root, word, 0)

    def _delete_helper(self, current, word, index):
        if index == len(word):
            if not current.is_end_of_word:
                return False
            current.is_end_of_word = False
            return len(current.children) == 0

        char = word[index]
        if char not in current.children:
            return False

        should_delete_current_node = self._delete_helper(current.children[char], word, index + 1)

        if should_delete_current_node:
            del current.children[char]
            return len(current.children) == 0

        return False

    def find_parent_node(self, word):
        current = self.root
        parent_node = None
        for char in word:
            if char not in current.children:
                return parent_node
            parent_node = current
            current = current.children[char]
        return parent_node

    def find_child_nodes(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return []
            current = current.children[char]

        child_nodes = []
        self._collect_child_nodes(current, word, child_nodes)
        return child_nodes

    def _collect_child_nodes(self, node, prefix, child_nodes):
        if node.is_end_of_word:
            child_nodes.append(prefix)

        for char, child in node.children.items():
            self._collect_child_nodes(child, prefix + char, child_nodes)

    def print_structure(self):
        self._print_structure_helper(self.root, "")

    def _print_structure_helper(self, node, prefix):
        if node.is_end_of_word:
            print(prefix)

        for char, child in node.children.items():
            self._print_structure_helper(child, prefix + char)


# Contoh penggunaan kamus Trie

kamus = Trie()

# Penyisipan kata-kata ke dalam kamus
kamus.insert("guava")
kamus.insert("ginger")
kamus.insert("apple")
kamus.insert("papaya")
kamus.insert("banana")
kamus.insert("ant")
kamus.insert("grape")
kamus.insert("water")
kamus.insert("camel")
kamus.insert("grapefruit")
kamus.insert("bear")
kamus.insert("corn")
kamus.insert("watermelon")

# Pencarian kata dalam kamus
print(kamus.search("apple"))  # True
print(kamus.search("mango"))  # True
print(kamus.search("laptop"))  # False
print("-----")

# Pencarian node parent
parent_node = kamus.find_parent_node("watermelon")
if parent_node:
    print("Parent node:", parent_node.children.keys())  # ['f']
else:
    print("Parent node not found")
print("-----")

# Pencarian node child
child_nodes = kamus.find_child_nodes("water")
if child_nodes:
    print("Child nodes:", child_nodes)  # ['grapefruit']
else:
    print("Child nodes not found")
print("-----")

# Penghapusan kata dari kamus
kamus.delete("apple")
print(kamus.search("apple"))  # False
print("-----")

# Tampilkan struktur pohon Trie
print("Struktur Pohon Trie:")
kamus.print_structure()

class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.is_word = True
    
    def exists(self, word):
      current_node = self.root
      for char in word:
        if char not in current_node.children:
          return False
        current_node = current_node.children[char]
      
      return current_node.is_word()

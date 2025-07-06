'''
Design a data structure that supports adding new words and searching for a string, where the search string may contain the dot character '.', which can match any letter.

Implement the WordDictionary class:
    + WordDictionary() — Initializes the object.
    + void addWord(word) — Adds a word into the data structure.
    + bool search(word) — Returns true if any previously added word matches the given word. The word can contain the dot character '.', which matches any single letter.

Example:
Input:  ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
        [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
Output: [null, null, null, null, false, true, true, true]

Разработайте структуру данных, поддерживающую добавление новых слов и поиск строки, где в строке поиска может использоваться символ '.', обозначающий любую букву.

Реализуйте класс WordDictionary с методами:
    + WordDictionary() — Инициализирует объект.
    + void addWord(word) — Добавляет слово в структуру данных.
    + bool search(word) — Возвращает true, если хотя бы одно из ранее добавленных слов совпадает с переданным словом. Символ '.' в слове может означать любую одну букву.

Пример:
Ввод:   ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
        [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
Вывод:  [null, null, null, null, false, true, true, true]
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root_node = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root_node
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def recursive_search(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_end_of_word

            current_character = word[index]

            if current_character == '.':
                for child_node in node.children.values():
                    if recursive_search(index + 1, child_node):
                        return True
                return False
            else:
                if current_character not in node.children:
                    return False
                return recursive_search(index + 1, node.children[current_character])

        return recursive_search(0, self.root_node)
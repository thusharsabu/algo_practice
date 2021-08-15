import copy
def findWords(board, words):
    word_list = create_trie(words)
    row_length = len(board)
    col_length = len(board[0])
    output = []

    visited_path = [[False for i in range(col_length)] for j in range(row_length)]

    def bt(row, column, word, current_trie, visited_):
        if(len(output) == len(words)): return

        if "*" in current_trie and word not in output:
            output.append(word)

        if row >= row_length or row < 0 or column >= col_length or column < 0:
            return

        if board[row][column] in current_trie:
            if visited_[row][column]:
                return

            # print(word)
            

            new_trie = current_trie[board[row][column]]

            new_word = word + board[row][column]
            # print(f"Word: {new_word}")
            print(f"Index: {row} {column} - Word {new_word}")

            print(visited_)
            visited_[row][column] = True
            bt(row + 1, column, new_word, new_trie, copy.deepcopy(visited_[:]))
            bt(row - 1, column, new_word, new_trie, copy.deepcopy(visited_[:]))
            bt(row, column + 1, new_word, new_trie, copy.deepcopy(visited_[:]))
            bt(row, column - 1, new_word, new_trie, copy.deepcopy(visited_[:]))

    for i in range(len(board)):
        for j in range(len(board[0])):
            print('---------')
            bt(i, j, "", word_list, copy.deepcopy(visited_path))

    return output


def create_trie(words):
    trie = {}
    for word in words:
        current = trie
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        # print(current)
        current["*"] = None
    return trie


# board = [
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
#     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
# ]
# words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
board = [["a","b"],["a","a"]]
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
print(findWords(board, words))

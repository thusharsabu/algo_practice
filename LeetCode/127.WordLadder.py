# Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence
# from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Return 0 if there is no such transformation sequence.

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


import copy


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_exist = False
        for char in wordList:
            if char == endWord:
                word_exist = True
        if not word_exist:
            return 0

        paths = self.ladder_length(wordList, beginWord, endWord)
        # print("The paths: {}".format(paths))
        if paths is not None and len(paths) > 0:
            first = paths[0]
            for ele in paths[1:]:
                if len(ele) < len(first):
                    first = ele
            return first
        else:
            return 0

    def ladder_length(self, words, current_word, endWord):
        # print("Begin: {}".format(current_word))
        # print("End: {}".format(endWord))
        # print("Array is: {}".format(words))
        # print("-------------------------")
        new_list = []

        for char in words:
            if char == endWord:
                # print(
                #     "Reached here: char is: {}, and EndWord: {}".format(char, endWord)
                # )
                new_list.append([char])
                return new_list
            if self.hamming_distance(char, current_word) == 1:
                new_words = copy.deepcopy(words)
                new_words.remove(char)
                value = self.ladder_length(new_words, char, endWord)

                if value != 0 and value is not None:
                    for each_ele in value:
                        each_ele.insert(0, char)
                        new_list.append(each_ele)

        if len(new_list) > 0:
            return new_list
        else:
            return 0

    def hamming_distance(self, str1, str2):
        hamming_dist = 0

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                hamming_dist += 1
        return hamming_dist


caller = Solution()
print(caller.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
# print(caller.ladderLength("lot", "cog", ["log", "cog"]))

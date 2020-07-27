'''
Category: String
Time Complexity: O(n)
'''


class Solution:
    def findAndReplacePattern(self, words: list, pattern: str):
        pattern_dict = {}
        i = 0
        p = ''
        answer = []
        for ch in pattern:
            if ch in pattern_dict.keys():
                p += str(pattern_dict[ch])
            else:
                pattern_dict[ch] = i
                p += str(i)
                i += 1
        for word in words:
            p_dict = {}
            w_i = 0
            w_p = ''
            for ch in word:
                if ch in p_dict.keys():
                    w_p += str(p_dict[ch])
                else:
                    p_dict[ch] = w_i
                    w_p += str(w_i)
                    w_i += 1
            if w_p == p:
                answer.append(word)
        return answer

    def findAndReplacePattern(self, words, pattern):
        answers = list()
        pattern_dict = dict()
        pattern_list = list()
        cur_num = -1
        cur_char = ''
        for i in range(0, len(pattern)):
            if cur_char == pattern[i]:
                pattern_list.append(pattern_dict[cur_char])
            else:
                cur_num += 1
                cur_char = pattern[i]
                if cur_char not in pattern_dict:
                    pattern_dict[cur_char] = cur_num
                pattern_list.append(pattern_dict[cur_char])

        for word in words:
            is_valid = True
            word_list = list()
            word_dict = dict()
            cur_word_num = -1
            cur_word_char = ''
            for i in range(0, len(word)):  # * n
                if cur_word_char == word[i]:
                    word_list.append(cur_word_num)
                else:
                    cur_word_num += 1
                    cur_word_char = word[i]
                    if cur_word_char not in word_dict:
                        word_dict[cur_word_char] = cur_word_num
                    if word_dict[cur_word_char] != pattern_list[i]:
                        is_valid = False
                        break
                    word_list.append(word_dict[cur_word_char])
            if is_valid and pattern_list == word_list:
                answers.append(word)
        return answers


words = ["qxrwtncxyoqwmsxoavos", "eqvzjrnqgkezxmqkhdkm",
         "pjxmgdujohpmtsjhazhs", "yqhlipeqwnylkrqnsbnr", "plktdyslmoptqflowaof"]
pattern = "ghtxpauhingxekhnoqnk"
# words = ["badc","abab","dddd","dede","yyxx"]
# pattern = "baba"
s = Solution().findAndReplacePattern(words, pattern)
print(s)

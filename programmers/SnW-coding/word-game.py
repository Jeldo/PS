def solution(n, words):
    answer = [0, 0]
    last_char = words[0][0]
    word_set = set()
    for i in range(len(words)):
        game_round, num = 0, 0
        if words[i][0] != last_char or words[i] in word_set:
            game_round, num = divmod(i + 1, n)
            game_round = game_round if num == 0 else game_round + 1
            num = n if num == 0 else num
            return [num, game_round]
        else:
            word_set.add(words[i])
        last_char = words[i][-1]
    return answer


# [3,3], [0,0], [1,3], (num, round)
cases = [
    (3, ['tank', 'kick', 'know', 'wheel', 'land',
         'dream', 'mother', 'robot', 'tank']),
    (5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure',
         'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']),
    (2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'])
]


for c in cases:
    s = solution(c[0], c[1])
    print(s)

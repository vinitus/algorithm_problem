def solution(keymap, targets):
    answer = [0 for _ in range(len(targets))]
    total_keymap = {}
    for key in keymap:
        for key_index in range(len(key)):
            word = key[key_index]
            if not total_keymap.get(word):
                total_keymap[word] = key_index + 1
            else:
                total_keymap[word] = min(total_keymap[word],key_index + 1)
    
    answer_index = 0
    for target in targets:
        for word in target:
            if not total_keymap.get(word):
                answer[answer_index] = -1
                break
            else:
                answer[answer_index] += total_keymap[word]
        answer_index += 1
                

    return answer
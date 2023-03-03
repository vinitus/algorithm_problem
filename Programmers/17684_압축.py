def solution(msg):
    answer = []

    dictionary = {}

    for i in range(1,27):
        dictionary[chr(i+64)] = i

    last_dict_index = 27
    index = 0
    max_length_minus_one = len(msg) - 1

    while index < len(msg):
        word = msg[index]
        answer += [1]
        while_2nd_index = index
        while dictionary.get(word):
            answer[-1] = dictionary[word]
            while_2nd_index += 1
            if while_2nd_index < len(msg):
                word += msg[while_2nd_index]
            else:
                index = len(msg) + 1
                break
        else:
            if not dictionary.get(word):
                dictionary[word] = last_dict_index
                last_dict_index += 1
                index = while_2nd_index - 1
        index += 1

    return answer
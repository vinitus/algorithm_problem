from heapq import heappush

def solution(scores):
    answer = 0
    
    small_score_dict = {}
    first_value_list = []
    
    me = scores[0]
    sum_me = sum(me)

    for score in scores:
        if small_score_dict.get(score[0]):
            small_score_dict[score[0]] = max(small_score_dict[score[0]],score[1])
        else:
            first_value_list.append(score[0])
            small_score_dict[score[0]] = score[1]
    
    first_value_list.sort(reverse=True)
    another_employee = len(scores)
    
    for first_value_index in range(first_value_list.index(me[0])):
        first_value = first_value_list[first_value_index]
        if small_score_dict[first_value] > me[1]:
            return -1
    
    scores.sort()
    
    incentive_dict = {}
    
    for index in range(another_employee):
        if sum(scores[index]) <= sum_me:
            continue
        
        stop_flag = False
        
        for first_value_index in range(first_value_list.index(scores[index][0])):
            first_value = first_value_list[first_value_index]
            if small_score_dict[first_value] > scores[index][1]:
                stop_flag = True
                break
        else:
            if not stop_flag:
                if not incentive_dict.get(sum(scores[index])):
                    incentive_dict[sum(scores[index])] = 1
                else:
                    incentive_dict[sum(scores[index])] += 1
    
    for rank_info in sorted(incentive_dict.items(), reverse=True):
        score, number = rank_info
        if sum(me) >= score:
            break
        else:
            answer += number
            
    answer += 1
    
    return answer
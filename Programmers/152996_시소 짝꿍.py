def solution(weights):
    answer = 0
    weight_list = list(0 for i in range(1001))
    
    for weight in weights:
        weight_list[weight] += 1
    
    for index in range(1001):
        if weight_list[index]:
            if weight_list[index] > 1:
                answer += weight_list[index] * (weight_list[index] - 1) // 2
            if index * 2 < 1001 and weight_list[index * 2]:
                answer += weight_list[index * 2] * weight_list[index]
            if index % 2 == 0 and index * 3 // 2 < 1001 and weight_list[index * 3 // 2]:
                answer += weight_list[index * 3 // 2] * weight_list[index]
            if index % 3 == 0 and index * 4 // 3 < 1001 and weight_list[index * 4 // 3]:
                answer += weight_list[index * 4 // 3] * weight_list[index]
                
    
    return answer
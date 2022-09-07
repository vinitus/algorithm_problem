# 삽입 정렬, 거품 정렬, 선택 정렬

# 거품 정렬은 이웃한 배열 내 원소의 크기를 비교하고 큰 원소를 뒤로 보내는 것
# 알고리즘을 짤 때는 처음부터 바꾼 원소까지 비교
# 외부 반목문은 뒤에서 부터 시작함
# 내부 반목문은 앞과 뒤를 계속 비교하는 방식
def bubble(tmp_list):
    for i in range(len(tmp_list)-1,0,-1):
        for j in range(i):
            if tmp_list[j] > tmp_list[j+1]:
                tmp_list[j], tmp_list[j+1] = tmp_list[j+1], tmp_list[j]

# 마지막 스왑의 위치를 기억함으로써 이미 정렬된 뒤쪽의 원소들은 비교할 필요가 없음
def bubble_fast(tmp_list):
    end = len(tmp_list)-1
    while end > 0:
        last_swap = 0
        for i in range(end,0,-1):
            for j in range(i):
                if tmp_list[j] > tmp_list[j+1]:
                    tmp_list[j], tmp_list[j+1] = tmp_list[j+1], tmp_list[j]
                    last_swap = i
            end = last_swap

# 선택
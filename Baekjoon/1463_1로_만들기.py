# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

N = int(input())

# 3으로 나누거나 2로 나누거나 -1을 했을 때 list에 추가
def to_1(tmp_list,count):
    count += 1
    result_list = []
    if len(tmp_list) > int(tmp_list[-1]/2):          # 매개변수 list의 큰 숫자들은 의미가 없음
        cal_index = int(tmp_list[-1]/2)
    else:
        cal_index = len(tmp_list)
    for i in range(cal_index):
        if tmp_list[i] % 3 == 0:
            result_list.append(int(tmp_list[i] / 3))
        if tmp_list[i] % 2 == 0:
            result_list.append(int(tmp_list[i] / 2))
        result_list.append(tmp_list[i] - 1)
    return result_list, count

count = 0                       # 연산 횟수를 세기 위한 count
result_cal_list = [N]           # 이 리스트에 /3 /2 -1을 한 결과들로 바꿔갈거임
if N == 1:
    print(0)
else:
    while True:
        result_cal_list, count = to_1(result_cal_list,count)
        result_cal_list = set(result_cal_list)      # set을 통해 중복 제거
        result_cal_list = list(result_cal_list)
        result_cal_list.sort()      # 가장 최소값을 찾기위해 정렬
        if result_cal_list[0] == 1: # 문제의 조건인 1을 찾으면 while문을 멈춤
            print(count)
            break
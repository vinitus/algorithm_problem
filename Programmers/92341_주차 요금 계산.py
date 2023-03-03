def solution(fees, records):
    dct = {}
    cars = []
    answer = []
    for record in records:
        record = record.split()
        tmp = list(map(int,record[0].split(':')))
        minute = tmp[0] * 60 + tmp[1]
        
        if record[2] == 'IN':
            cars.append(record[1])
            if not dct.get(record[1]):
                dct[record[1]] = -minute
            else:
                dct[record[1]] += -minute
        else:
            dct[record[1]] += minute
            cars.remove(record[1])
    while cars:
        minute = 23*60 + 59
        car = cars.pop()        
        dct[car] += minute
    for key, value in sorted(dct.items()):
        value -= fees[0]
        if value <= 0:
            answer.append(fees[1])
        else:
            if value % fees[2] != 0:
                answer.append(fees[1] + fees[3] * (value // fees[2] + 1))
            else:
                answer.append(fees[1] + fees[3] * (value // fees[2]))
    return answer
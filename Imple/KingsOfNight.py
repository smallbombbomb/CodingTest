#현재 나이트 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동 가능한 방향 8가지
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대해 각 위치 이동
result = 0
for step in steps:
    #이동할 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치 이동 가능하면 카운트 증가
    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
        result += 1


print(result)
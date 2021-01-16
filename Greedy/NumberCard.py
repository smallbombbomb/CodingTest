# N, M 공백 구분하여 입력받기
n, m = map(int, input().split())

result = 0

# 한줄씩 입력받기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은수
    min_value = min(data)
    # 가장 작은수중 가장 큰수
    result = max(result, min_value)

    print(result)
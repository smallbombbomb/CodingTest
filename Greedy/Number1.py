# 최대한 많이 나누기
# 나머지 1이면 1빼기
# N, K 공백으로 입력받음
n, k = map(int, input().split())

result = 0


while True:
    # (n == k로 나누어 떨어지기까지 1씩빼기)
    target = (n // k) * k
    #print(target)
    result += (n - target)
    n = target
    # N이 K보다 적을때(더이상 못나눌떄) break
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

    result += (n - 1)
    print(result)

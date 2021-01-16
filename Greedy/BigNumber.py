# N, M, K 공백 구분
n, m, k = map(int, input().split())
# N개의 수 공백 구분
data = list(map(int, input().split()))

data.sort() #배열정렬
first = data[n - 1] #첫번째 큰수
second = data[n -2] #두번째 큰수

#가장 큰수 더해지는 연산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) + first # 가장 큰수 더하기
result += (m - count) * second # 두번쨰 큰수 더하기

print(result)
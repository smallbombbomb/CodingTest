# 반복적 구현
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 수 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적 구현
def factorial_recursive(n):
    if n <= 1: # n이 1이하는 1
        return 1
    # n! = n * (n - 1)
    return n * factorial_recursive(n - 1)

#반복, 재귀적 팩토리얼 출력
print('반복적 구현 : ', factorial_iterative(5))
print('재귀적 구현 : ', factorial_recursive(5))
def recursive_function(i):
    # 100번째 출력시 종료
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수까지 호출')
    recursive_function(i + 1)
    print(i, '번째 재귀함수 종료')

recursive_function(1)
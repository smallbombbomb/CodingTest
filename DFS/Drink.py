# N,M 공백 입력

n, m = map(int, input().split())

# 2차원 리스트 입력정보
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드 방문 이후 연결된 모든 노드들도 방문
def dfs(x, y):
    # 범위 벗어나는경우 종료
    if x<= -1 or x>= n or y <= -1 or y >= m:
        return False
    # 노드 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당노드 방문처리
        graph[x][y] = 1
        #상, 하, 좌, 우 위치 재귀적 호출
        dfs(x - 1, y)   #좌
        dfs(x, y - 1)   #상
        dfs(x + 1, y)   #우
        dfs(x, y + 1)  #하
        return True
    return False

# 모든 노드(위치)에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)

 #BFS : 너비 우선 탐색
from collections import deque

# BFS 메서드정의
def bfs(graph, start, visited):
    #큐(Queue) 구현위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드 방문처리
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end= ' ')
        # 해당 원소와 연결된, 아직방문하지 않은 원소 큐에 삽입
        for i in graph[v]:
             if not visited[i]:
                 queue.append(i)
                 visited[i] = True

# 각노드가 연결된정보 리스트 자료형 표현(2차원)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각노드가 방문한 정보 리스트 자료형 표시
visited = [False] * 9

# 정의된 BFS 함수
bfs(graph, 1, visited)
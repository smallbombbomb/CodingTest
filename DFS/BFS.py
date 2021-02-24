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
         
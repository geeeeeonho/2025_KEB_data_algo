# 깊이우선탐색(dfs)
def dfs(g, i, visited):  # g=graph , i=A B C D E ,visited=[]
    visited[i] = 1  # 방문리스트에서 i에 해당하는 문자에 해당하는 칸을 1로
    print(chr(ord('A') + i), end=' ')
    for j in range(len(g)):  # 장소의 길이만큼 이동
        # 경로가 존재         방문한 리스트에서 없으면
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)
    """
    A->B
    B->D
    D->C
    C~>D    D->E
    E->F
    """


from collections import deque  # for bfs


# deque=선입선출
# 너비우선탐색(bfs)
def bfs(g, i, visited):  # g=graph , i=A B C D E ,visited=[]
    queue = deque([i])  # i=0값을 가진 queue 생성
    visited[i] = 1  # 방문리스트에서 i에 해당하는 문자에 해당하는 칸을 1로
    while queue:
        i = queue.popleft()  # dequeue
        print(chr(ord('A') + i), end=' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)  # enqueue
                visited[j] = 1
    """
    1. 시작 노드 A(0)를 큐에 추가 -> queue = [A], visited = [1, 0, 0, 0, 0, 0]
    2. A를 탐색하고 제거 -> queue = [], visited = [1, 1, 1, 0, 0, 0]
       - A와 연결된 B, C를 큐에 추가 -> queue = [B, C]
    3. B를 탐색하고 제거 -> queue = [C], visited = [1, 1, 1, 1, 0, 0]
       - B와 연결된 D를 큐에 추가 -> queue = [C, D]
    4. C를 탐색하고 제거 -> queue = [D], visited = [1, 1, 1, 1, 0, 0]
       - C와 연결된 D는 이미 방문됨 (추가 X)
    5. D를 탐색하고 제거 -> queue = [], visited = [1, 1, 1, 1, 1, 1]
       - D와 연결된 E, F를 큐에 추가 -> queue = [E, F]
    6. E를 탐색하고 제거 -> queue = [F]
    7. F를 탐색하고 제거 -> queue = []

    최종 출력: A B C D E F

    if 4(E)에서 시작했다면
    E D F B C A
    """


graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]
"""
A - B - D - E
 ＼    /  ＼ |
    C       F

"""

visited = [0 for _ in range(len(graph))]
# dfs(graph, 0, visited)
bfs(graph, 0, visited)
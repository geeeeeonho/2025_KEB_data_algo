class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]  # 인접 행렬로 그래프 표현


# 그래프 출력 함수
def print_graph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(name_ary[v], end=' ')  # 도시 이름 출력
    print()
    for row in range(g.SIZE):
        print(name_ary[row], end=' ')  # 행의 시작에 도시 이름 출력
        for col in range(g.SIZE):
            print(f"{g.graph[row][col]:2}", end=' ')  # 가중치 출력 (2칸 확보)
        print()
    print()


# 깊이 우선 탐색 (DFS) - 특정 정점이 존재하는지 확인
def dfs(g, current, find_vtx, visited):
    visited.append(current)  # 현재 노드를 방문한 목록에 추가
    if current == find_vtx:  # 찾으려는 정점인지 확인
        return True
    for vertex in range(g.SIZE):
        if g.graph[current][vertex] != 0 and vertex not in visited:
            if dfs(g, vertex, find_vtx, visited):  # 연결된 정점으로 이동하여 탐색
                return True
    return False


# 특정 정점이 그래프 내에서 연결되어 있는지 확인하는 함수
def find_vertex(g, find_vtx):
    visited = []
    return dfs(g, 0, find_vtx, visited)  # 0번 정점(춘천)에서 시작하여 탐색


# 그래프 생성 및 초기화
G1 = None
name_ary = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5  # 도시를 인덱스로 매핑

g_size = 6
G1 = Graph(g_size)

# 간선(도로) 추가 (양방향 그래프)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

# 초기 그래프 출력
print_graph(G1)

# 간선 목록 생성 (가중치, 시작 정점, 도착 정점)
edge_ary = []
for i in range(g_size):
    for k in range(g_size):
        if G1.graph[i][k] != 0:  # 가중치가 0이 아닌 경우 간선으로 추가
            edge_ary.append([G1.graph[i][k], i, k])

print(edge_ary, len(edge_ary))  # 생성된 간선 목록과 개수 출력

# 가중치를 기준으로 내림차순 정렬 (가중치가 큰 간선이 먼저)
edge_ary.sort(reverse=True)

print(edge_ary, len(edge_ary))  # 정렬된 간선 목록과 개수 출력

# 중복 간선 제거 (양방향 그래프이므로 중복 제거)
new_ary = []
for i in range(0, len(edge_ary), 2):  # 두 개씩 건너뛰며 하나씩 저장
    new_ary.append(edge_ary[i])

print(new_ary, len(new_ary))  # 중복 제거된 간선 목록 출력

# 크루스칼 알고리즘을 응용하여 최소 신장 트리 생성 (불필요한 간선 제거)
index = 0
while len(new_ary) > g_size - 1:  # 최소 신장 트리 조건 (정점 개수 - 1개의 간선 유지)
    start = new_ary[index][1]  # 현재 간선의 시작점
    end = new_ary[index][2]  # 현재 간선의 도착점
    save_cost = new_ary[index][0]  # 가중치 저장

    # 그래프에서 해당 간선 제거
    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    # 간선을 제거한 후에도 그래프가 여전히 연결되어 있는지 확인
    startYN = find_vertex(G1, start)
    endYN = find_vertex(G1, end)

    if startYN and endYN:  # 여전히 연결되어 있다면 간선 삭제 유지
        del new_ary[index]
    else:  # 삭제하면 연결이 끊어지므로 복원
        G1.graph[start][end] = save_cost
        G1.graph[end][start] = save_cost
        index += 1  # 다음 간선 확인

# 최종 최소 신장 트리 출력
print_graph(G1)
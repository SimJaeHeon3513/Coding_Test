import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

matrix = []
ans = 0

def dfs(node):
    global ans
    # leaf면 0 리턴
    if not matrix[node]:
        return 0
    
    # 자식들의 최대 깊이 구하기
    child_depths = []
    for child, w in matrix[node]:
        child_depths.append(w + dfs(child))
    
    max_depth = max(child_depths)
    
    # 최대 깊이 기준으로 나머지 증가량 계산
    for d in child_depths:
        ans += max_depth - d
    
    return max_depth

T = int(input())

for _ in range(T):
    test_case = int(input())
    matrix = [[] for _ in range(test_case)]
    ans = 0

    for i in range(1, test_case):
        p, w = map(int, input().split())
        matrix[p].append((i, w))

    for i in range(test_case):
        matrix[i].sort(key=lambda x: x[1], reverse=True)

    dfs(0)
    print(ans)
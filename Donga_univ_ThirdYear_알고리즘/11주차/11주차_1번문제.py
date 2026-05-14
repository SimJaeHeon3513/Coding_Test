import sys

MOD = 1000007
MAX = 2000

# 조합 C[n][r] 미리 계산
C = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for i in range(MAX + 1):
    C[i][0] = 1
    C[i][i] = 1
    for j in range(1, i):
        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def ways(p, q):
    dx = abs(p[0] - q[0])
    dy = abs(p[1] - q[1])
    return C[dx + dy][dx]


def path_count(points):
    total = dist(points[0], points[-1])
    dsum = 0
    result = 1

    for i in range(len(points) - 1):
        dsum += dist(points[i], points[i + 1])
        result = (result * ways(points[i], points[i + 1])) % MOD

    if dsum == total:
        return result
    return 0


T = int(sys.stdin.readline())

for _ in range(T):
    sx, sy, tx, ty, ax, ay, bx, by = map(int, sys.stdin.readline().split())

    S = (sx, sy)
    T_point = (tx, ty)
    A = (ax, ay)
    B = (bx, by)

    count_A = path_count([S, A, T_point])
    count_B = path_count([S, B, T_point])

    count_AB = path_count([S, A, B, T_point])
    count_BA = path_count([S, B, A, T_point])

    answer = (count_A + count_B - count_AB - count_BA) % MOD

    print(answer)
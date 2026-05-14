import math

def solve(n):
    limit = math.isqrt(n)

    for k in range(1, 5):
        result = dfs(n, limit, k)
        if result:
            return result


def dfs(remain, max_root, count):
    if count == 0:
        if remain == 0:
            return []
        return None

    for x in range(min(max_root, math.isqrt(remain)), 0, -1):
        rest = dfs(remain - x * x, x, count - 1)

        if rest is not None:
            return [x] + rest

    return None


while True:
    n = int(input())

    if n == 0:
        break

    result = solve(n)
    print(str(n) + "=" + "+".join(str(x) + "^2" for x in result))
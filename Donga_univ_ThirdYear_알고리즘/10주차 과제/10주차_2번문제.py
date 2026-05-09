import sys
input = sys.stdin.readline


def kmp_search(text, pattern):
    n = len(pattern)

    pi = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    j = 0

    for x in text:
        while j > 0 and x != pattern[j]:
            j = pi[j - 1]

        if x == pattern[j]:
            j += 1

            if j == n:
                return True

    return False


def reverse_polygon(arr):
    n = len(arr)
    result = []

    for i in range(n - 1, -1, -1):
        length = abs(arr[i])

        if arr[(i - 1) % n] > 0:
            result.append(-length)
        else:
            result.append(length)

    return result


T = int(input())

for _ in range(T):
    N = int(input())

    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    doubled = s1 + s1
    reversed_s1 = reverse_polygon(s1)
    doubled_reversed = reversed_s1 + reversed_s1

    if kmp_search(doubled, s2) or kmp_search(doubled_reversed, s2):
        print(1)
    else:
        print(0)
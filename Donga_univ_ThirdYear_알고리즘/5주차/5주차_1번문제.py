import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    students = int(input())
    first_line = list(map(int. input().split()))
    last_line = list(map(int. input().split()))

    result = [0] * students

    for fl in first_line[::-1]:
        if fl in last_line:
            result[fl-1] = first_line.index(fl) - last_line.index(fl)
            first_line.remove(fl)
            last_line.remove(fl)

    print(*result)
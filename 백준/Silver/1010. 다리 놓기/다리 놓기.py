t = int(input())

def bionomial_coefficient(k, n):
    if(k > n-k):
        k = n-k
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) // i
    return result

for i in range(t):
    n, m = map(int, input().split())
    print(bionomial_coefficient(n, m))
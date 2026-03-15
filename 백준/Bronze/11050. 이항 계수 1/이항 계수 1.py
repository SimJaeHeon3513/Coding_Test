def factorial(a):
    if(a == 1 or a == 0):
        return 1
    else:
        return a * factorial(a-1)

n, k = map(int, input().split())

print(factorial(n) // (factorial(k) * factorial(n-k)))
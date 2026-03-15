def prime(k):
    if(k == 0) or (k == 1):
        return False   
    for i in range(2, int(k**(0.5)+1)):
        if(k % i == 0):
            return False
    return True

n = int(input())
for i in range(n):
    t = int(input())
    while(True):
        if prime(t):
            print(t)
            break
        else:
            t += 1
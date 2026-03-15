n = int(input())
a = 2

if(n == 1):
    print("")
    
else:
    while(n != 1):
        if(n%a == 0):
            print(a)
            n = n/a
        else:
            a += 1
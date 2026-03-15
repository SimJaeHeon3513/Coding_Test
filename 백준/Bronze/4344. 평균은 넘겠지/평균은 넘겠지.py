c = int(input())

for _ in range(c):
    subject = list(map(int, input().split()))
    avg = sum(subject[1:]) / subject[0]
    check = 0
    for j in subject[1:]:
        if(j > avg):
            check += 1

    result = (check / subject[0]) * 100
    print("%0.3f"%result+"%")
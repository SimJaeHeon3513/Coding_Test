def solution(mats, park):
    mats.sort(reverse=True)
    
    
    for mat in mats:
        for r in range(len(park) - mat + 1):
            for c in range(len(park[0]) - mat + 1):
                check = True
                
                for i in range(mat):
                    for j in range(mat):
                        if park[r + i][c + j] != "-1":
                            check = False
                            break
                    if not check:
                        break
                
                if check:
                    return mat
    return -1
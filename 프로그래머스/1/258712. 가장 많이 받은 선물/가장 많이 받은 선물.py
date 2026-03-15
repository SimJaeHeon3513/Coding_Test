def solution(friends, gifts):
    answer = 0
    
    friends_idx = {name: i for i, name in enumerate(friends)}
    print(friends_idx)
    
    table = [[0] * (len(friends)+1) for _ in range(len(friends)+1)]
    print(table)
    
    gift_indices = [0] * (len(friends))
    
     
    for g in gifts:
        give, receive = g.split(" ")
        table[friends_idx[give]][friends_idx[receive]] += 1
        gift_indices[friends_idx[give]] += 1
        gift_indices[friends_idx[receive]] -= 1
        
    print(table)
    print(gift_indices)

    next_month_gifts = [0] * len(friends)
    
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if table[i][j] > table[j][i]:
                next_month_gifts[i] += 1
            elif table[i][j] < table[j][i]:
                next_month_gifts[j] += 1
            elif table[i][j] == table[j][i]:
                if gift_indices[i] > gift_indices[j]:
                    next_month_gifts[i] += 1
                elif gift_indices[i] < gift_indices[j]:
                    next_month_gifts[j] += 1
            
    answer = max(next_month_gifts)
            
            
    return answer



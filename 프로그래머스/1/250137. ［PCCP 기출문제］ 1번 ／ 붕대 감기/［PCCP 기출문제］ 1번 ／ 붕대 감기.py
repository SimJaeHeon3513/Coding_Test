def checking_health(ch, h):
    if ch > h:
        return min(ch, h)
    elif ch <= 0:
        return -1
    else:
        return ch

def solution(bandage, health, attacks):
    answer = 0
    bandage_time = 0
    current_health = health
    
    attack_moment = 0
    
    for i in range(1, attacks[-1][0]+1):
        
        if i == attacks[attack_moment][0]:
            current_health -= attacks[attack_moment][1]
            bandage_time = 0
            current_health = checking_health(current_health, health)
            if current_health == -1:
                return -1
            attack_moment += 1
            
            
        else:
            current_health += bandage[1]
            bandage_time += 1
        
            if bandage_time == bandage[0]:
                current_health += bandage[2]
                current_health = checking_health(current_health, health)
                bandage_time = 0
            
        current_health = checking_health(current_health, health)
        
            
        print(i, current_health,health)        
        
    answer = current_health
    return answer
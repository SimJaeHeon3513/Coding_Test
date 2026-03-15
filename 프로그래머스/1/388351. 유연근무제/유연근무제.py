def solution(schedules, timelogs, startday):
    answer = 0
    
    for i, row in enumerate(timelogs):
        is_fail = False
        current_day = startday
        hour, minute = divmod(schedules[i]+10,100)
        h, m = divmod(minute, 60)
        limit_time = ((hour + h) * 100) + m
        
        for time in row:
            if current_day < 6:
                pass
                if time > limit_time:
                    is_fail = True
                    break
            current_day += 1 
            if current_day > 7:
                current_day = 1
        
        if not is_fail:
            answer += 1
        
    return answer
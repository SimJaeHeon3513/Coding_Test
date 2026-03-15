def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def change_StrToInt(t):
        return int(t.replace(":", ""))
    
    def change_IntToStr(t):
        string = str(t).zfill(4)
        return string[0:2] + ":" + string[2:]
    
    def change_MinToSec(t):
        m, s = divmod(t, 100)
        return (m * 60) + s
    
    def change_SecToMin(t):
        m, s = divmod(t, 60)
        return (m * 100) + s
    
    def op_checking(t, s, e):
        if s <= t <= e:
            return e
        return t
    
    vl = change_MinToSec(change_StrToInt(video_len))
    ps = change_MinToSec(change_StrToInt(pos))
    op_s = change_MinToSec(change_StrToInt(op_start))
    op_e = change_MinToSec(change_StrToInt(op_end))
    
    
    print(op_s, op_e)
    for c in commands:
        ps =op_checking(ps, op_s, op_e)
            
        if c == "prev":
            ps = max(0, ps - 10)
        else:
            ps = min(vl, ps + 10)
        
        ps =op_checking(ps, op_s, op_e)
                  
    
    return change_IntToStr(change_SecToMin(ps))
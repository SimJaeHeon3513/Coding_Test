def solution(data, ext, val_ext, sort_by):
    a = []
    answer = []
    
    if ext == "code":
        for d in data:
            if d[0] < val_ext:
                a.append(d)
    elif ext == "date":
        for d in data:
            if d[1] < val_ext:
                a.append(d)
    elif ext == "maximum":
        for d in data:
            if d[2] < val_ext:
                a.append(d)
    elif ext == "remain":
        for d in data:
            if d[3] < val_ext:
                a.append(d)
                
    if sort_by == "code":
        answer = sorted(a, key = lambda x : x[0])
    elif sort_by == "date":
        answer = sorted(a, key = lambda x : x[1])
    elif sort_by == "maximum":
        answer = sorted(a, key = lambda x : x[2])
    elif sort_by == "remain":
        answer = sorted(a, key = lambda x : x[3])
            
                
                  
    return answer
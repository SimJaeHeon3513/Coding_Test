# 1. GCD 직접 구현
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 2. LCM 직접 구현
def get_lcm(a, b):
    if a == 0 or b == 0: return 0
    return (a * b) // get_gcd(a, b)

def solution(signals):
    # 1. 모든 신호등의 주기(T) 리스트 만들기
    periods = [sum(s) for s in signals]
    
    total_lcm = sum(signals[0])
    for i in range(1, len(signals)):
        current_period = sum(signals[i])
        total_lcm = get_lcm(total_lcm, current_period)
    
    # 3. 1초부터 LCM까지 탐색
    for t in range(1, total_lcm + 1):
        all_yellow = True
        
        for i in range(len(signals)):
            G, Y, R = signals[i]
            T = periods[i]
            
            current_signal_time = (t - 1) % T
            
            if not (G <= current_signal_time < G + Y):
                all_yellow = False
                break
        
        # ★ 이 위치가 중요합니다! (모든 신호등 검사 직후)
        if all_yellow:
            return t
            
    return -1
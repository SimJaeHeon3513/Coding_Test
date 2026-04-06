def solution(info, n, m):
    # dp[j]는 도둑 B의 흔적이 j일 때, 도둑 A 흔적의 최솟값
    # 초기값은 아주 큰 값(INF)으로 설정
    INF = float('inf')
    dp = [INF] * m
    dp[0] = 0  # 시작 시점: B의 흔적 0, A의 흔적 0

    for a_trace, b_trace in info:
        new_dp = [INF] * m
        for j in range(m):
            if dp[j] == INF:
                continue
            
            # 1. A가 훔치는 경우
            if dp[j] + a_trace < n:
                new_dp[j] = min(new_dp[j], dp[j] + a_trace)
            
            # 2. B가 훔치는 경우
            if j + b_trace < m:
                new_dp[j + b_trace] = min(new_dp[j + b_trace], dp[j])
        
        dp = new_dp

    # 모든 물건을 훔친 후 dp 테이블에서 가장 작은 값 찾기
    answer = min(dp)
    return answer if answer != INF else -1
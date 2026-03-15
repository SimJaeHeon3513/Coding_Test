def solution(n, w, num):
    # 1. 특정 번호의 (행, 열) 위치를 반환하는 함수
    def get_pos(val, w):
        row = (val - 1) // w
        col = (val - 1) % w
        # 홀수 행이면 열 번호를 반전 (오른쪽에서 왼쪽으로)
        if row % 2 == 1:
            col = (w - 1) - col
        return row, col

    # 2. 찾으려는 상자의 위치 구하기
    target_row, target_col = get_pos(num, w)
    
    # 3. 전체 상자의 최대 행 번호 계산
    max_row = (n - 1) // w
    
    answer = 0
    # 4. 타겟 상자 행부터 맨 위 행까지 올라가며 확인
    for r in range(target_row, max_row + 1):
        # 현재 검사하는 행(r)과 타겟 열(target_col)에 들어올 실제 숫자 역계산
        # 열 위치(c)를 다시 번호로 바꿀 때는 해당 행의 방향을 고려해야 함
        
        # 행 r에서의 열 위치 계산 로직을 거꾸로 적용
        if r % 2 == 0:
            current_col_val = (r * w) + (target_col + 1)
        else:
            current_col_val = (r * w) + ((w - 1 - target_col) + 1)
            
        # 계산된 숫자가 전체 상자 개수 n 이내라면 상자가 존재하는 것임
        if current_col_val <= n:
            answer += 1
            
    return answer
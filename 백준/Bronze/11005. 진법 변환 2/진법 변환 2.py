n_str, b_str = input().split()
n = int(n_str)
base = int(b_str)

def convert_base(n, base):
    if n == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while n > 0:
        # 매개변수 이름을 일치시켜야 합니다 (base)
        result = digits[n % base] + result
        n //= base
        
    return result

print(convert_base(n, base))
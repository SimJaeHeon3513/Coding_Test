n = int(input())

x_max, x_min = -10000, 10000
y_max, y_min = -10000, 10000

while(n):
    x, y = map(int, input().split())
    
    if x > x_max:
        x_max = x 
    if x < x_min:
        x_min = x
    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y
    n -= 1

print((x_max - x_min) * (y_max - y_min))
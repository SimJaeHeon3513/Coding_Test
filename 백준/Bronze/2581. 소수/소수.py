n1 = int(input(""))
n2 = int(input(""))
num = []
for i in  range(n1, n2+1):
  check = 0
  if i > 1:
    for j in range(2, i):
      if(i % j == 0):
        check = 1
        break
    if(check == 0):
      num.append(i)

if len(num) > 0:
  print(sum(num))
  print(min(num))
  
else:
  print("-1")


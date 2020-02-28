N = int(input())
Earnings = []
Sum_list = []

for i in range(N):
    a = int(input())
    Earnings.append(a)


for i in Earnings:
    if i != 0:
        Sum_list.append(i)
    if i == 0:
        Sum_list.pop()

Sum = 0
if len(Sum_list) == 0:
    print(0)
else:
    for i in Sum_list:
        Sum += i 
        
    print(Sum)
N = int(input())
Totals = []
# Creating Lists with Interger Inputs
for i in range(2):
    a = input().split(" ")
    a = list(map(int,a))
    Totals.append(a)

Sum1 = 0
Sum2 = 0
K = 0
for i in range(0,N):
    Sum1 += Totals[0][i]
    Sum2 += Totals[1][i]
    if Sum1 == Sum2:
        K = i + 1 

print(K)





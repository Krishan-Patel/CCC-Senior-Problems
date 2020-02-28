type = int(input())
N = int(input())
a = input().split(" ")
a = list(map(int,a))
b = input().split(" ")
b = list(map(int,b))

if type == 1: # Finding the Minimum
    a.sort()
    b.sort()
    sum = 0
    for i in range(N):
        if a[i] <= b[i]:
            sum += b[i]
        else: 
            sum += a[i]
    print(sum)

if type == 2: # Finding the Maximum 
    a.sort()
    b.sort(reverse = True)
    sum = 0 
    for i in range(N):
        if a[i] <= b[i]:
            sum += b[i]
        else: 
            sum += a[i]
    print(sum)
    


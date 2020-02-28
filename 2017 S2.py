N = int(input())
tides = []
a = input().split(" ")
a = list(map(int,a))
tides = a 
tides.sort()

if N % 2 != 0:
    Odd = True 
else: 
    Odd = False

if Odd == False: 
    y = int(N/2)
    for i in range(y):
        print(tides[y-1-i], end=" ")
        print(tides[y+i], end=" ")
else: 
    y = int(N/2)
    print(tides[y], end=' ')
    for i in range(1,y+1):
        print(tides[y+i], end =' ')
        print(tides[y-i], end=' ')
print('')



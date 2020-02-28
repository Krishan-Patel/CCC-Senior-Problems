N = int(input())
a = input().split(" ")
b = input().split(" ")
partners = []
bad = False
# Crete partners list 
for i in range(N):
    z = []
    if a[i] != b[i]:
        z.append(a[i])
        z.append(b[i])
        partners.append(z)
    else: 
        bad = True

if bad == False:
    x = 0
    for i in partners:
        for y in range(N-1,x,-1):
            if (i[0] == partners[y][1] and i[1] != partners[y][0]) or (i[1] == partners[y][0] and i[0] != partners[y][1]):
                bad = True        
        x += 1 

if bad == True:
    print("bad")
else: 
    print("good")


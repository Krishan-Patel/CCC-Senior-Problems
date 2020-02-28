N , M =list(map(int,input().split(" ")))
Grid = []
Camera = []
Convoys = []
Objectives = []
Me = []

# Create a Grid with all the inputs
for i in range(N):
    a = list(input())
    Grid.append(a)
print(Grid)

def seen(x,y):
    n= 1
    seen1 = False
    seen2 = False
    seen3 = False
    seen4 = False
    while seen1 == False:
        if Grid[x][y+n] == "W":
            seen1 = True
        elif Grid[x][y+n] == ".":
            a = [x,y+n]
            Camera.append(a)
    n = 1 
    while seen2== False:
        if Grid[x][y-n] == "W":
            seen2 = True
        elif Grid[x][y-n] == ".":
            a= [x,y-n]
            Camera.append(a)
    n = 1 
    while seen3 == False:
        if Grid[x+n][y] == "W":
            seen3 = True
        elif Grid[x+n][y] == ".":
            a = [x+n,y]
            Camera.append(a)
    n = 1 
    while seen4 == False:
        if Grid[x-n][y] == "W":
            seen4 = True
        elif Grid[x-n][y] == ".":
            a = [x,y]
            Camera.append(a)


for x in range(N):
    
    for y in range(M):
        if Grid[x][y] == ".":
            if Grid[x-1][y] == "W" and Grid[x+1][y] == 'W' and Grid[x][y-1] == 'W' and Grid[x][y+1] == 'W':
                print(-1)
                #
            else: 
                a = [x,y]
                Objectives.append(a)
        if Grid[x][y] == "L" or "U" or "R" or "D":
            a = [x,y]
            Convoys.append(a)
        if Grid[x][y] == "C":
            seen(x,y)
        if Grid[x][y] == "S":
            a = [x,y]
            Me.append(a)

print(Me)




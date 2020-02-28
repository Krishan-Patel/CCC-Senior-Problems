N = int(input())
grid = []
# Create Input
for i in range(N):
    a = input().split(" ")
    a = list(map(int,a))
    grid.append(a)
      
horiztonal_inc = False
vertical_inc = False 
# Test if the numbers are increasing going up/down and left/right
if grid[0][0] < grid[0][1]:
    horizontal_inc = True
else:
    horizontal_inc = False

if grid[0][0] < grid[1][0]:
    vertical_inc = True
else: 
    vertical_inc = False

# determines the orientation of the garden 
if vertical_inc == False and horizontal_inc == False:
     for j in range(N,0,-1):
        for y in range(N,0,-1):
            print(grid[j-1][y-1], end='')
            print(' ', end='')
        print("")

elif vertical_inc == False and horizontal_inc == True: 
    for z in range(N):
        for j in range(N,0,-1):
            print(grid[j-1][z], end='')
            print(" ", end='')
        print("")
elif vertical_inc == True and horizontal_inc == False:
    for z in range(N,0,-1):
        for y in range(N):
            print(grid[y][z-1] , end= '')
            print(' ',end= '')
        print("")
    
else:
    for z in range(N):
        for y in range(N):
            print(grid[z][y], end='')
            print(" ", end='')
        print("")

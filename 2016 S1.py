a = input()
b = input()
L1 = []
L2 = []
anagram = True
for i in a:
    L1.append(i)
for i in b:
    L2.append(i)
counter = 0

for x in range(len(L1)): 
    for y in range(len(L1)):
        if L1[x] == L2[y]:
            L1[x] = 2
            L2[y] = 2
            counter += 1 
            break

for i in range(counter):
    L1.remove(2)
    L2.remove(2)
    
if len(L1) == 0:
    print("A")
else:
    for i in L2:
        if i != "*":
            anagram = False
    if anagram == False: 
        print("N")
    else:
        print("A")



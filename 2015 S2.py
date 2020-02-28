
J = int(input())
A = int(input())
Jersey = []
Athletes = []

for i in range(J):
    Jersey.append((input()))

for i in range(A):
    a = input().split(" ")
    a[1] = int(a[1])
    Athletes.append(a)

outcomes = 0 

for x in Athletes:
    index = x[1] - 1 
    if Jersey[index] != "T":
        if Jersey[index] == x[0] or (x[0] == "M" and Jersey[index] == "L") or (x[0] == "S" and Jersey[index] == "L") or (x[0] == "S" and Jersey[index] == "M"):
            outcomes += 1 
            Jersey[index] = "T"
    

print(outcomes)

points = []
N = int(input()) #store the number of villages

# Creates a list with the village position 
def listing_Villages():
    for i in range(N):
        points.append(int(input()))
        points.sort() #sorts the list in ascending order 

def finding_difference(x):
    difference = (points[x] - points[x-1]) + (points[x+1] - points[x])
    return difference / 2 

def smallest_neighbourhood():
    smallest_neighbourhood = finding_difference(1)
    for i in range (2,N-1):
        diff = finding_difference(i)
        if diff < smallest_neighbourhood:
            smallest_neighbourhood = diff
    return smallest_neighbourhood

listing_Villages()
print(smallest_neighbourhood())










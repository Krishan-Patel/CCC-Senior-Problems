inputs = []
x = int(input())
def create_list():
    for i in range(x):
        inputs.append(int(input()))

def check_prime(integer):
    factors = 0
    for number in range (2,integer):
        if integer % number == 0:
            factors += 1
    if factors != 0: 
        return False
    else:
        return True
        
def average_of_primes():
    for num in inputs:
        sum_of_primes = 2*num
        for a in range (2,num): 
            b = sum_of_primes - a 
            if check_prime(a) and check_prime(b): 
                print(a,b)
                break
           
create_list()
average_of_primes()

 

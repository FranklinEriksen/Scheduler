import math #for gcd func
import random

def miller(n,rounds):
    s = 0
    d = n-1
    while d%2==0:
        d = int(d/2)
        s+=1 
 
    for i in range(rounds):#number of trials 
        a = random.randrange(2, n)
        if pow(a, d, n) == 1:
            return "Likely Prime"

        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return "Likely Prime"

        return "Composite"
 
    return "Likely Prime"  


def g(x,n):
    return (x**2 + 1) % n

def pollards(n):
    denom = 1
    x = 2
    y = 2
    while denom == 1:
        x = g(x,n)
        y = g(g(y,n),n)
        denom = math.gcd(abs(x-y),n)

    if denom == n: 
        return -1
    else:
        return denom


if __name__ == "__main__":
    x = 31531
    y = 520482


    print(str(x) + " is " + str(miller(x, 10)) )
    print(str(y) +  " is " + str(miller(y, 10)) )

    print("Factor of " + str(x) + ": " + str(pollards(x)) )
    print("Factor of " + str(y) + ": " + str(pollards(y)) )
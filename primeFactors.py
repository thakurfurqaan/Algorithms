import math 

def primeFactors(n): 
    prime_factors = []
    while n % 2 == 0: 
        prime_factors.append(2) 
        n = n / 2 
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            prime_factors.append(i) 
            n = n / i 
    if n > 2: 
        prime_factors.append(n) 
    print(prime_factors)
  
n = 315
print("Prime Factors of " + str(n) + ":     ")
primeFactors(n) 
def is_prime(num):
    count=0
    for i in range(1, num+1):
        if num%i==0:
            count+=1
    return True if count==2 else False
    

def find_twin_primes(limit):
    twin_primes = []
    for i in range(3, limit, 2):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

twin_primes = find_twin_primes(1000)
for twin in twin_primes:
    print(twin)
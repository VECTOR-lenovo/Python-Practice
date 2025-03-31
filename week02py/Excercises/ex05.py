num=int(input("Enter the number: "))
def sumOfDivisors(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    if divisors_sum==num:
        print(f"The number{num} is a perfect number")
    else:
        print(f"The number {num} is not a perfect number ")    
sumOfDivisors(num)

def prodDigits(number):
    product = 1
    while number > 0:
        digit = number % 10
        product *= digit
        number= number//10  
    return product
number=int(input("Enter the number: "))
print(prodDigits(number))

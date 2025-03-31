def multiply_all(*nums):
    result = 1
    for i in nums:
        result *= i
    return result
print(multiply_all(1, 2, 3, 4, 5))
print(multiply_all(12, 13, 14)) 